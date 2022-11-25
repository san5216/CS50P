from numb3rs import validate

def test_validate_too_high():
    assert validate("1.2.3.500") is False

def test_validate():
    assert validate("255.255.0.0") is True

def test_validate_first_byte():
    assert validate("255.275.289.500") is False

def test_validate_invalid_format():
    assert validate("127.0.cat.1") is False
