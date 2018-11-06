def convert(rates, value, current, to):
    if current == to:
        value = 1
        return value
    for x in rates:
        if current == x[1] and to == x[2]:
            return value * x[0]
    for x in rates:
        if current == x[2] and to == x[1]:
            return value / x[0]