def read_next(*args):
    for iterable in args:
        for j in iterable:
            yield j
