import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar(capacity=12)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(capacity=12)
    jar.deposit(7)
    assert jar.size() == 7
    with pytest.raises(ValueError):
        assert jar.deposit(13)


def test_withdraw():
    jar = Jar(capacity=12)
    jar.deposit(7)
    assert jar.withdraw(5) == 2
    with pytest.raises(ValueError):
        assert jar.withdraw(13)
