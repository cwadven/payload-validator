import unittest

from payload_validator.error_contexts import NormalValidatorErrorContext


class TestValidatorErrorContext(unittest.TestCase):
    def test_normal_validator_error_context(self):
        # Given: Create an instance of NormalValidatorErrorContext
        context = NormalValidatorErrorContext()

        # When: Add an error
        context.add_error("field1", "error1")

        # Then: Check that the error was added correctly
        self.assertEqual(context["field1"], ["error1"])

        # When: Add another error to the same field
        context.add_error("field1", "error2")

        # Then: Check that the new error was appended correctly
        self.assertEqual(context["field1"], ["error1", "error2"])
