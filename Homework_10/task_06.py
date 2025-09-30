import re


def is_password_strong(password: str) -> bool:
    """
        Checks if password contains:
            more than 8 characters
            at least one digit
            at least one uppercase letter
            at least one lowercase letter
            at least one special character
    """

    pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%&*!]).{8,}$")
    return bool(re.match(pattern, password))


# tests
passwords = [
    "Password1@",
    "weakpass",
    "SHORT1!",
    "NoSpecial123",
    "Valid#Pass1"
]
# {
# 'Password1@': True,
# 'weakpass': False,
# 'SHORT1!': False,
# 'NoSpecial123': False,
# 'Valid#Pass1': True
# }
print({p: is_password_strong(p) for p in passwords})
