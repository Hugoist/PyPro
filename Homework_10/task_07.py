import re


def find_ipv4(text: str) -> list[str]:
    """
    Find the IPv4 address from a string
    """

    pattern = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
    )

    return pattern.findall(text)


# tests
s = "Valid: 192.168.0.1, 10.0.0.255. Invalid: 999.999.999.999, 256.100.50.25"
# ['192.168.0.1', '10.0.0.255']
print(find_ipv4(s))
