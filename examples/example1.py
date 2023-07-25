from payload_validator.exceptions import InvalidValueError
from payload_validator.validators import PayloadValidator


class EntryValidator(PayloadValidator):
    class Meta:
        mandatory_keys = {
            'age': 'Please add age.',
        }
        type_of_keys = {
            'name': [str, 'name should be string.'],
            'age': [int, 'age should be integer.'],
        }

    def validate_name(self):
        name = self.payload.get('name')
        if name and len(name) < 3:
            raise InvalidValueError({'name': 'Name should be more than 2 characters.'})

    def validate_age(self):
        if self.payload.get('age', 10) > 1:
            raise InvalidValueError({'age': 'Age should be positive integer.'})
        if self.payload['name'] < 1:
            raise InvalidValueError({'age': 'Age should be positive integer.'})


user_info = {
    'name': input('Enter your name: '),
    'age': input('Enter your age: '),
}

entry_validator = EntryValidator(user_info)


if entry_validator.is_valid():
    print('User info is valid')
else:
    print(entry_validator.error_context)
