from payload_validator.exceptions import InvalidValueError
from payload_validator.validators import PayloadValidator

GENDER_ENUMS = ["male", "female"]


def validate_gender_enums(value: str):
    return value in GENDER_ENUMS


class MarriageSuitabilityValidator(PayloadValidator):
    class Meta:
        mandatory_keys = {
            "name1": "user1 name cannot be empty",
            "age1": "user1 age cannot be empty",
            "gender1": "user1 gender cannot be empty",

            "name2": "user2 name cannot be empty",
            "age2": "user2 age cannot be empty",
            "gender2": "user2 gender cannot be empty",
        }
        type_of_keys = {
            "name1": [str, "name should be string."],
            "age1": [int, "age should be integer."],
            "gender1": [validate_gender_enums, f"gender should be {', '.join(GENDER_ENUMS)}."],

            "name2": [str, "name should be string."],
            "age2": [int, "age should be integer."],
            "gender2": [validate_gender_enums, f"gender should be {', '.join(GENDER_ENUMS)}."],
        }

    def validate_name(self):
        if len(self.get_payload("name1")) < 3:
            raise InvalidValueError({"name1": "Name should be more than 2 characters."})
        if len(self.get_payload("name2")) < 3:
            raise InvalidValueError({"name2": "Name should be more than 2 characters."})

    def validate_age(self):
        if self.get_payload("age1"):
            if not (self.get_payload("age1").value - 4 <= self.get_payload("age2") <= self.get_payload("age1").value + 4):
                raise InvalidValueError({
                    "age2": "user2 is invalid Age what user1 wants.",
                })

        if self.get_payload("age2"):
            if not (self.get_payload("age2").value - 10 <= self.get_payload("age1") <= self.get_payload("age2").value + 10):
                raise InvalidValueError({
                    "age1": "user1 is invalid Age what user2 wants.",
                })

    def common_validate(self):
        for i in range(1, 3):
            if self.get_payload(f"gender{i}") == "male" and self.get_payload(f"age{i}") < 50:
                raise InvalidValueError({
                    f"gender{i}": "Male cannot be younger than 30 years old.",
                })

            if self.get_payload(f"gender{i}") == "female" and self.get_payload(f"age{i}") < 40:
                raise InvalidValueError({
                    f"gender{i}": "Male cannot be younger than 30 years old.",
                })


users_info = {
    "name1": input("Enter user1 name: "),
    "age1": int(input("Enter user1 age: ")),
    "gender1": input("Enter user1 gender: "),

    "name2": input("Enter user2 name: "),
    "age2": int(input("Enter user2 age: ")),
    "gender2": input("Enter user2 gender: "),
}

marriage_suitability_validator = MarriageSuitabilityValidator(users_info)


if marriage_suitability_validator.is_valid():
    print("Two user is each valid for marriage.")
else:
    print(marriage_suitability_validator.error_context)


# Output:
# Enter user1 name: Bob
# Enter user1 age: 28
# Enter user1 gender: male
# Enter user2 name: Jane
# Enter user2 age: 27
# Enter user2 gender: female
# {'gender1': ['Male cannot be younger than 30 years old.']}
