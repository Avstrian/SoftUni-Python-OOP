def reverse_text(string):
    start = string.index(string[-1])
    while not start < 0:
        yield string[start]
        start -= 1
