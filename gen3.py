def string_characters(s):
    for ch in s:
        yield ch
for c in string_characters("Python"):
    print(c)
