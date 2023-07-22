from typing import Dict


class ValidationException(Exception):
    def __init__(self):
        super().__init__(self, "Validation failed")


class ValidationNotRunException(Exception):
    pass


class MismatchedErrorKeysException(Exception):
    pass


class InvalidValueError(Exception):
    def __init__(self, error_value_by_key: Dict[str, str], skip_existing_errors: list = None):
        if skip_existing_errors is None:
            skip_existing_errors = []
        result = [key for key in skip_existing_errors if key not in error_value_by_key.keys()]
        if result:
            raise MismatchedErrorKeysException(f"In error_exists_skip_keys {', '.join(result)} not in error_value_by_key")
        self.error_value_by_key = error_value_by_key
        self.skip_existing_errors = skip_existing_errors
