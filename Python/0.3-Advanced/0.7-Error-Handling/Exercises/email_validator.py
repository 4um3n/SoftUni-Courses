import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_email_pattern = r"^([A-Za-z\d]+)(@)?[A-Za-z]+(\.[A-Za-z]+)+$"
valid_domains = [".com", ".bg", ".org", ".net"]
email_data = input()
while email_data:
    try:
        name, at, domain = re.findall(valid_email_pattern, email_data)[0]
    except (IndexError, ValueError):
        email_data = input()
        continue

    if len(name) < 5:
        raise NameTooShortError(f"Name must be more than 4 characters")

    if not at:
        raise MustContainAtSymbolError(f"Email must contain @")

    if domain not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")

    print(f"Email is valid")
    email_data = input()
