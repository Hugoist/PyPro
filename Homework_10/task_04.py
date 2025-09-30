import re


def reformat_date(date_str: str) -> str | None:
    """
     Reformat the date string from DD/MM/YYYY to YYYY-MM-DD
    """
    pattern = re.compile(
        r"(0[1-9]|[12][0-9]|3[01])"  # day: 01-09, 10-29, 30-31
        r"/"
        r"(0[1-9]|1[0-2])"  # month: 01-09, 10-12
        r"/"
        r"(\d{4})"  # year: 4 digits
    )
    match = pattern.fullmatch(date_str)
    if match:
        day, month, year = match.groups()
        return f"{year}-{month}-{day}"
    return None


dates = [
    "30/09/2025",
    "32/13/2322",
    "123/3/2312",
    "tr"
]
# {
#   '30/09/2025': '2025-09-30',
#   '32/13/2322': None,
#   '123/3/2312': None,
#   'tr': None}
print({d: reformat_date(d) for d in dates})
