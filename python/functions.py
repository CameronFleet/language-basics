def divide(a: int, b: int) -> float:
    return a / b

def add(a: int, b: int, allow_negative: bool = True):
    if (a < 0 or b < 0) and not allow_negative:
        raise ValueError(f"Negative value provided {a}, {b}")
    return a + b

print(divide(5, 5))
print(divide(10, 5))
print(add(10, 5))
print(add(10, -5))
print(add(10, -5, allow_negative=False))



