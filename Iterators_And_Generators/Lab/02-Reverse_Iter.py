class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        temp = self.iterable[self.current]
        self.current -= 1
        return temp
