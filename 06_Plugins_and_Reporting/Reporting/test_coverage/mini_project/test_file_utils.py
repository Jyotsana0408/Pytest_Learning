

from file_utils import get_extension, is_text_file

def test_get_extension():
    assert get_extension("document.txt") == "txt"

def test_is_text_file():
    assert is_text_file("notes.txt") is True
    assert is_text_file("image.png") is False
