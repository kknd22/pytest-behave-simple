import pytest
from calc.calculator import Calculator

def test_add():
    c = Calculator()
    result = c.add2(3, 4)
    assert result == 7

