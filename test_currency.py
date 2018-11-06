from currency import convert

# def test_convert_when_same():
#     assert convert([], 1, "USD", "USD") == 1

def test_convert_when_forward():
    assert convert([(0.74, "USD", "EUR")], 1, "USD", "EUR") == 0.74

def test_convert_when_backward():
    assert round(convert([(0.74, "USD", "EUR")], 1, "EUR", "USD"), 2) == 1.35