import unittest
from payload_validator.exceptions import (
    InvalidValueError,
    MismatchedErrorKeysException,
    ValidationException,
    ValidationNotRunException,
)


class TestValidationException(unittest.TestCase):
    def test_validation_exception(self):
        # Given:
        # When:
        try:
            raise ValidationException()
        # Then:
        except ValidationException as e:
            self.assertEqual(e.args[1], "Validation failed")


class TestValidationNotRunException(unittest.TestCase):
    def test_validation_not_run_exception(self):
        # Given:
        # When:
        try:
            raise ValidationNotRunException()
        # Then:
        except ValidationNotRunException as e:
            self.assertEqual(e.__class__.__name__, "ValidationNotRunException")


class TestMismatchedErrorKeysException(unittest.TestCase):
    def test_mismatched_error_keys_exception(self):
        # Given:
        # When:
        try:
            raise MismatchedErrorKeysException()
        # Then:
        except MismatchedErrorKeysException as e:
            self.assertEqual(e.__class__.__name__, "MismatchedErrorKeysException")


class TestInvalidValueError(unittest.TestCase):
    def test_invalid_value_error_exception_should_success_when_without_skip_existing_errors(self):
        # Given:
        error_value_by_key = {"key1": "error1", "key2": "error2"}

        # When:
        error = InvalidValueError(error_value_by_key)

        # Then:
        self.assertEqual(error.error_value_by_key, error_value_by_key)
        self.assertEqual(error.skip_existing_errors, [])

    def test_invalid_value_error_exception_should_success_when_skip_existing_errors(self):
        # Given:
        error_value_by_key = {"key1": "error1", "key2": "error2"}
        skip_existing_errors = ["key2"]

        # When:
        error = InvalidValueError(error_value_by_key, skip_existing_errors)

        # Then:
        self.assertEqual(error.error_value_by_key, error_value_by_key)
        self.assertEqual(error.skip_existing_errors, skip_existing_errors)

    def test_invalid_value_error_exception_should_raise_when_skip_existing_errors_not_exists_in_error_value_by_key(self):
        # Given: not exists skip_existing_errors in error_value_by_key
        error_value_by_key = {"key1": "error1", "key2": "error2"}
        invalid_keys = ["invalid_key", "invalid_key2"]

        # When:
        with self.assertRaises(MismatchedErrorKeysException) as context:
            InvalidValueError(error_value_by_key, invalid_keys)

        # Then: invalid_key and invalid_key2 should be in error message
        self.assertEqual(
            str(context.exception),
            "In error_exists_skip_keys {} not in error_value_by_key".format(
                "invalid_key, invalid_key2"
            )
        )
