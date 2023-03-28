# numbers
print(f"1: {type(1)}")
print(f"1.0: {type(1.0)}")
print(f"{2**64}: {type(2**64)}")
print(f"{5/2}: {type(5/2)}")
print(f"{5/2}: {type(5//2)}")


# text
print(f"'abc': {type('abc')}")
print("""
    multi-line string
""")

# bool
print(f"True: {type(True)}")
print(f"False: {type(False)}")


# lists
word = 'Python'
print(f"{word[0]}: {type(word[0])}")
print(f"{word[1:3]}: {type(word[1:3])}")
print(f"{word[-2:]}: {type(word[-2:])}")


squares = [1, 4, 9, 16, 25]
print(f"{squares[0]}")
print(f"{squares[-1]}")
print(f"{squares[-3:]}")
print(f"shallow copy: {squares[:]}")
print(f"concat: {squares + [36]}")

squares[0] = 9
print(f"lists are mutable: {squares[0]}")

# other
print(f"{0xFFFFFF}, {type(0xFFFFFF)}")