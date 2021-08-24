class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dictionary):
            current_index = self.index
            self.index += 1
            items = list(self.dictionary.items())
            return items[current_index]
        else:
            raise StopIteration
