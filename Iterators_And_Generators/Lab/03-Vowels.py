class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.vowels_list = "AEIOUYaeiouy"
        self.vowels = [el for el in self.string if el in self.vowels_list]
        self.vowels.reverse()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.vowels) == 0:
            raise StopIteration
        return self.vowels.pop()
