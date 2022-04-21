class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) not in range(5, 16):
            raise ValueError(f"The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, value):
        if not self.chek_password_length(value) or not self.check_password_for_digit(value)\
                or not self.check_password_for_upper(value):
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    @staticmethod
    def chek_password_length(password):
        return False if len(password) < 8 else True

    @staticmethod
    def check_password_for_digit(password):
        return True if any([char for char in password if char.isdigit()]) else False

    @staticmethod
    def check_password_for_upper(password):
        return True if any([char for char in password if char.isupper()]) else False
    
    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'
