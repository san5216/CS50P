import bank


def test_value_with_hello():
    assert bank.value("Hello") == 0
    assert bank.value("hello") == 0


def test_value_starts_h():
    assert bank.value("hi") == 20
    #assert bank.value("HI") == 20
    #assert bank.value("Howdy") == 20


def test_value_not_h():
    assert bank.value("Aloha") == 100
    #assert bank.value("Allo") == 100


def test_value_not_letters():
    assert bank.value("12345") == 100