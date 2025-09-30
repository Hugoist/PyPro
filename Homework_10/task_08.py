import re


def extract_urls(text: str) -> list[str]:
    """
    Extract urls from a string
    """

    pattern = re.compile(r"(https?://\S+|www\.\S+)")
    return re.findall(pattern, text)


# tests
text = "Ось посилання: https://example.com/test, а також www.test.ua і http://site.org/page?id=1"
print(extract_urls(text))
# ['https://example.com/test', 'www.test.ua', 'http://site.org/page?id=1']
