import re


class User:
    """ Class representing a user """

    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name

        if self.basic_validate_email(email):
            self.__email = email
        else:
            raise ValueError("Invalid email")

        print('User created successfully')

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __repr__(self):
        return f'User({self.first_name}, {self.last_name}, {self.email})'

    def basic_validate_email(self, email):
        email_validate_pattern = r"^\S+@\S+\.\S+$"
        return re.match(email_validate_pattern, email)


user1 = User("John", "Smith", "o@lo.lo")  # User created successfully
print(user1)  # User(John, Smith, o@lo.lo)

print(user1.first_name)  # John
print(user1.last_name)  # Smith
print(user1.email)  # o@lo.lo

user1.first_name = "Oleksandr"
user1.last_name = "Lupa"
user1.email = "ko@ko.ko"

print(user1)  # User(Oleksandr, Lupa, ko@ko.ko)

try:
    user2 = User("John", "Smith", "o@lo")  # Invalid email
except ValueError as e:
    print(e)
