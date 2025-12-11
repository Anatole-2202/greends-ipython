import pytest
from jar import Jar

def test_init():
    jar=Jar()
    assert (jar.capacity) == 12

def test_str():
    jar=Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"

def test_deposit():
    jar=Jar()
    jar.deposit(2)
    assert (jar.size) == 2
#we dont use assert below because if we put : jar.deposit(13) before the assert
# the program will stop before raching the assert because of the ValueError
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar=Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert (jar.size) == 8
    with pytest.raises(ValueError):
        jar.withdraw(11)
