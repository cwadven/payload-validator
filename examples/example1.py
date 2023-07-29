from payload_validator.exceptions import InvalidValueError
from payload_validator.validators import PayloadValidator


class EntryValidator(PayloadValidator):
    class Meta:
        mandatory_keys = {
            "name": "Please add name",
            "age": 'Please add age.',
        }
        type_of_keys = {
            "name": [str, "name should be string."],
            "age": [int, "age should be integer."],
        }

    def validate_name(self):
        if len(self.get_payload("name")) < 3:
            raise InvalidValueError({"name": "Name should be more than 2 characters."})

    def validate_age(self):
        if self.get_payload("age") < 1:
            raise InvalidValueError({"age": "Age should be positive integer."})

        if self.get_payload("age") and self.get_payload('age').value + 8 < 10:
            raise InvalidValueError({"age": "Age should be more than 2."})


user_info = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: ")),
}

entry_validator = EntryValidator(user_info)


if entry_validator.is_valid():
    print('User info is valid')
else:
    print(entry_validator.error_context)


# Output:
# Enter your name: 1
# Enter your age: 1
# {'name': ['Name should be more than 2 characters.'], 'age': ['Age should be more than 2.']}
