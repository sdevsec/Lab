import pytest
from account import Account

def test_init():
    # Test the __init__ method of the Account class
    acc = Account("John")
    assert acc.get_name() == "John"
    assert acc.get_balance() == 0

def test_deposit():
    # Test the deposit method of the Account class
    acc = Account("John")
    assert acc.deposit(100) == True
    assert acc.get_balance() == 100
    assert acc.deposit(-50) == False  # Cannot deposit negative amount
    assert acc.get_balance() == 100  # Balance should remain unchanged
    assert acc.deposit(0) == False  # Cannot deposit zero amount
    assert acc.get_balance() == 100  # Balance should remain unchanged

def test_withdraw():
    # Test the withdraw method of the Account class
    acc = Account("John")
    acc.deposit(100)
    assert acc.withdraw(50) == True
    assert acc.get_balance() == 50
    assert acc.withdraw(-50) == False  # Cannot withdraw negative amount
    assert acc.get_balance() == 50  # Balance should remain unchanged
    assert acc.withdraw(0) == False  # Cannot withdraw zero amount
    assert acc.get_balance() == 50  # Balance should remain unchanged
    assert acc.withdraw(100) == False  # Cannot withdraw more than current balance
    assert acc.get_balance() == 50  # Balance should remain unchanged
