from django.core.exceptions import ValidationError


def username_isalpha_validator(value: str):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters.")


# def image_max_size_validator(max_size_in_mb):
#     def internal_validator(value):
#         file_size = value.file.size
#         max_size_in_bytes = max_size_in_mb * 1024 * 1024
#
#         if file_size > max_size_in_bytes:
#             raise ValidationError("Max file size is 5.00 MB")
#
#     return internal_validator


def image_max_size_validator(value):
    file_size = value.file.size
    max_size_in_bytes = 5 * 1024 * 1024

    if file_size > max_size_in_bytes:
        raise ValidationError("Max file size is 5.00 MB")


