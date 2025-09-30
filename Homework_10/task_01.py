import re


def validate_email(email: str) -> bool:
    """
    Validate simple email format
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return bool(re.fullmatch(pattern, email))


# tests
emails = ["ivan@example.com", "test.email+filter@domain.ua", "invalid-email@", "@domain.ua"]
print({e: validate_email(e) for e in emails})