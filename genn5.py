def uppercase_generator(s):
    for ch in s:
        yield ch.upper()
for char in uppercase_generator("PyThOn"):
    print(char)
