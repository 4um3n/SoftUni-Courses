import re
from django.core.exceptions import ValidationError


def username_validator(value):
    username_pattern = r"^\w+$"

    if not re.match(username_pattern, value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
