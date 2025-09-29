from file_processor import FileProcessor
import pytest


# Fixture for creating FileProcessor instance
def test_file_write_read(tmpdir):
    file = tmpdir.join("testfile.txt")
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(file)
    assert content == "Hello, World!"


def test_empty_string(tmpdir):
    file = tmpdir.join("empty.txt")
    FileProcessor.write_to_file(file, "")
    content = FileProcessor.read_from_file(file)
    assert content == ""


def test_large_data(tmpdir):
    file = tmpdir.join("large.txt")
    large_text = "ololo\n" * 10000
    FileProcessor.write_to_file(file, large_text)
    content = FileProcessor.read_from_file(file)
    assert content == large_text


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        FileProcessor.read_from_file("non_existing.txt")


@pytest.mark.parametrize("data", ["ololo\n", "12345\n", "йцукен\n"])
def test_parametrized_write_read(tmpdir, data):
    file = tmpdir.join("param.txt")
    FileProcessor.write_to_file(file, data)
    content = FileProcessor.read_from_file(file)
    assert content == data
