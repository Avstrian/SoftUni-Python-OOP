def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(num, sequence):
        result = []
        for i in range(num):
            result.append(next(sequence))

        return result

    return take, halves, integers
