import re


def remove_html_tags(content: str) -> str:
    """
    Removes HTML tags from a string
    """

    return re.sub(r'<.*?>', '', content)


# tests
sample_text = "<p>Hello World!</p>"
print(remove_html_tags(sample_text))
# "Hello World!"
