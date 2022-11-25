from twttr import shorten


def test_shorten_upper():
    assert shorten("HELLO") == "HLL"

def test_shorten_mixed():
    assert shorten("HELlO") == "HLl"

def test_shorten_sentence():
    assert shorten("Hello, World!") == "Hll, Wrld!"

def test_shorten_numbers():
    assert shorten("123456789") == "123456789"

