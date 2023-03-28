def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError()
    return a / b

if __name__ == '__main__':
    try:
        divide(5, 0)
    except ZeroDivisionError as e:
        print(f"Got 0 division error: {e}")
    
    divide(1, 0)