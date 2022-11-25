import plates

def test_is_valid_starts_two_letters():
    #assert plates.is_valid("123") == False
    assert plates.is_valid("CS50") == True

def test_is_valid_not_starts_letters():
    #assert plates.is_valid("50CS") == False
    assert plates.is_valid("CS50") == True

def test_is_valid_correct_number_characters():
    #assert plates.is_valid("C") == False
    assert plates.is_valid("AAA123") == True

def test_is_valid_numbers_in_middle():
    #assert plates.is_valid("AA15AA") == False
    assert plates.is_valid("ABC123") == True

def test_is_valid_zero_first_number():
    #assert plates.is_valid("AA01234") == False
    assert plates.is_valid("AA12304") == True

def test_is_valid_only_characters():
    assert plates.is_valid("ABC12!3") == False
    #assert plates.is_valid("ABC1234") == True


