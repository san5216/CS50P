from working import convert
import pytest


def test_convert():
    assert convert("5:00 AM to 3:00 PM") == "05:00 to 15:00"


def test_convert_no_to():
    with pytest.raises(Exception):
        assert convert("9 AM - 5 PM") == "09:00 to 17:00"


def test_convert_high_minutes():
    with pytest.raises(Exception):
        assert convert("9:60 AM to 5:60 PM") == "09:60 to 17:60"
