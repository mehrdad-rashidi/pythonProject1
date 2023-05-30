class PowTwo:
    def __init__(self, maxValue=0):
        self.maxValue = maxValue

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        if self.number <= self.maxValue:
            result = 2 ** self.number
            self.number += 1
        else:
            raise StopIteration

