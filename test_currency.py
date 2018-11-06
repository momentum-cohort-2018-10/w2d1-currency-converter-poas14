import pytest
from currency import convert

def test_convert_when_same():
    assert convert([], 1, "USD", "USD") == 1

def test_that_is_not_1():
    assert convert([(0.74, "USD", "EUR")], 4, "USD", "EUR") == 2.96

def test_convert_when_forward():
    assert convert([(0.74, "USD", "EUR")], 1, "USD", "EUR") == 0.74

def test_convert_when_backward():
    assert round(convert([(0.74, "USD", "EUR")], 1, "EUR", "USD"), 2) == 1.35

def test_multiple_tuples():
    assert round(convert([(0.74, "USD", "EUR"), (145.949, "EUR", "JPY")], 4, "EUR", "USD"), 2) == 5.41
"""Note: Is it acceptable to run each one by chaning the questioning number? I guess it would be obviously considerably slower..."""

def test_convert_when_unknown():
    assert() convert([(1.31, "GBP", "USD")], 6, "GBP, EUR") == ValueError