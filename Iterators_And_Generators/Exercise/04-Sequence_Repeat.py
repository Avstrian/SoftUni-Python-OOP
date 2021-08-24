class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence_listed = list(sequence)
        self.number = number
        self.index = 0
        self.printed_numbers = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.printed_numbers < self.number:
            if self.index == len(self.sequence_listed):
                self.index = 0
            current_index = self.index
            self.index += 1
            self.printed_numbers += 1
            return self.sequence_listed[current_index]
        else:
            raise StopIteration()
