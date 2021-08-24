class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        has_number = False
        for char in value:
            if char.isdigit():
                has_number = True
        if value.islower() or len(value) < 8 or not has_number:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        coded_pass = ["*" for char in self.__password]
        return f'You have a profile with username: "{self.__username}" and password: {"".join(coded_pass)}'
