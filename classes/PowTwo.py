class PowTwo:
    def __init__(self, maxValue=0):
        self.maxValue = maxValue
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.maxValue:
            result = 2 ** self.number
            self.number += 1
            return result
        else:
            raise StopIteration

