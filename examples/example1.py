from datetime import datetime
from pprint import pprint

from payload_validator.exceptions import (
    InvalidValueError,
    ValidationException,
)
from payload_validator.validators import PayloadValidator


def validate_date_parsing(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except (TypeError, ValueError):
        return False


# 1
class NewPayloadValidator(PayloadValidator):
    # 2
    DEFAULT_MANDATORY_ERROR_MESSAGE = 'mandatory data missing'

    class Meta:
        # 3-1, 3-2
        mandatory_keys = {
            'displayable': 'displayable is required',
            'mode': 'mode is always required',
            'amount': 'why are you not setting amount?',
            'minimum_order_value': 'minimum order value is required',
            'applicable_order_types': 'really you are not setting applicable order types?',
            'start_date': 'start date is required',
            'end_date': 'end date is required for your job',
        }
        # 3-1, 3-3
        type_of_keys = {
            'amount': [int, 'integer_type_needs'],
            'minimum_order_value': [int, 'integer_type_needs'],
            'maximum_download_count': [(int, type(None)), 'integer_type_needs or NoneType'],
            # 3-4
            'start_date': [validate_date_parsing, 'need to be date type'],
            'end_date': [validate_date_parsing, 'need to be date type'],
        }

    # 4-1, 4-2
    def validate_hello_world(self):
        if not self.get_payload('displayable'):
            # 4-3, 4-4
            raise InvalidValueError({'displayable': 'displayable is false'})

    # 4-1, 4-2
    def validate_max_length(self):
        if self.get_payload('max_length') <= 0:
            # 4-3, 4-4, 4-5, Extra
            self.add_error_and_skip_validation_key(
                'max_length',
                [
                    'validate_max_length: This max_length should be inside error context1',
                    'validate_max_length: This max_length should be inside error context2',
                ],
            )

    def validate_min_length(self):
        if self.get_payload('min_length') <= 0:
            # 4-3, 4-4
            raise InvalidValueError(
                {
                    'min_length': 'validate_min_length: This min_length should be inside error context',
                },
            )

    # 5
    def common_validate(self):
        if self.get_payload('max_length') < self.get_payload('min_length'):
            raise InvalidValueError(
                {
                    'max_length': 'This Should be not exists in error context'
                                  'because of at `validate_max_length` function'
                                  'add_error_and_skip_validation_key method has max_length error context',
                    'min_length': 'This Should be not exists in error context'
                                  'because of validate_min_length method has min_length error context'
                                  'and this InvalidValueError has ignore_existing_error_keys of mix_length',
                },
                ignore_existing_error_keys={'min_length'},
            )

        if True:
            raise InvalidValueError(
                {
                    'max_length': 'This Should be not exists in error context'
                                  'because of upper logic has man_length error context'
                                  'and this InvalidValueError has ignore_existing_error_keys of max_length',
                    'min_length': 'common_validate: This min_length should be inside error context',
                },
                ignore_existing_error_keys={'max_length'},
            )


validator = NewPayloadValidator(
    {'displayable': True, 'start_date': 1, 'min_length': 0, 'max_length': 0}
)

try:
    # 7
    validator.validate()
except ValidationException as e:
    print('[ validate method ]')
    pprint(validator.error_context)

# 8
if not validator.is_valid():
    print('[ is_valid method ]')
    pprint(validator.error_context)
