import pytest
from jar import Jar

def test_init():
    # Valid capacity
    Jar(capacity=12)
    Jar(capacity=20)
    Jar(capacity=36)

    # Invalid capacity
    with pytest.raises(ValueError):
        Jar(capacity=-1)
        Jar(capacity=-10)
        Jar(capacity=-100)

def test_str():
    jar = Jar()

    assert str(jar) == ""
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    jar = Jar(capacity=20)
    assert str(jar) == ""
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    jar = Jar(capacity=36)
    assert str(jar) == ""
    jar.deposit(20)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()

    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(89)

    jar = Jar(capacity=20)
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(21)

    jar = Jar(capacity=36)
    jar.deposit(20)
    assert jar.size == 20
    with pytest.raises(ValueError):
        jar.deposit(37)


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(64)

    jar = Jar(capacity=20)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(21)

    jar = Jar(capacity=36)
    jar.deposit(20)
    jar.withdraw(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.withdraw(37)
