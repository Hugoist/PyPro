import re


def extract_hashtags(text: str) -> list[str]:
    """ Extract hashtags from text """

    pattern = re.compile(r"(?<!\w)#[a-zA-ZА-Яа-яҐґЄєІіЇї0-9]+(?=\b)")
    return re.findall(pattern, text)


# tests
text = "#Lorem ip#sum #2025 #python3 #text_with_underscore #тест #ї"
print(extract_hashtags(text))  # ['#Lorem', '#2025', '#python3', '#тест', '#ї']
