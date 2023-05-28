# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from utility import util
from functools import reduce
import math
import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
'''
    Numeric Literals are immutable (unchangeable). Numeric literals 
    can belong to 3 different numerical types: Integer, Float, and Complex
'''
# print with end whitespace
# Notice that we have included the end= ' ' after the end of the first print() statement.
print('Good Morning!', end=' ')
print('It is rainy today')
# Hence, the output includes items separated by . not comma.
print('New Year', 2023, 'See you soon!', sep='. ')
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x, y))
# using input() to take user input
# num = input('Enter a number: ')
# print('You Entered:', num)
# print('Data type of num:', type(num))
languages = ['Swift', 'Python', 'Go']

for _ in languages:
    print('Hello')
    print('Hi')
util.add_numbers(12, 13)
var = lambda: print('Hello World')
var()
# lambda that accepts one argument
greet_user = lambda name: print('Hey there,', name)
upgrade = lambda self, value, args, offset=0, limit=None, order=None, count=False: value if count else self.browse(
    value)
list1 = [2, 4, 6, 8]
print(list1)


def add_five(number):
    return number + 5


print(list1)
new_list = list(map(add_five, list1))

print(new_list)
new_list1 = list(map(lambda x1: x1 + 5, list1))

print(new_list1)

numbers = [1, 4, 5, 10, 20, 30]
print(numbers)


def greater_than_ten_func(number):
    if number > 10:
        return True
    else:
        return False


new_numbers = list(filter(greater_than_ten_func, numbers))

print(new_numbers)

new_numbers1 = list(filter(lambda x2: x2 > 10, numbers))
print(new_numbers1)

numbers = [10, 20, 30, 40]
print(numbers)

result = reduce(lambda a, b: a + b, numbers)
print(result)
print(dir(math.__name__))
print(0b1101011)  # prints 107
print(0xFB + 0b10)  # prints 253
print(0o15)  # prints 13
print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']
# get random item from list1
print(random.choice(list1))
# Shuffle list1
random.shuffle(list1)
# Print the shuffled list1
print(list1)
# Print random element
print(random.random())
numbers = [21, 34, 54, 12]
numbers1 = [number * number for number in range(1, 6)]
print(numbers1)
print([numbers * x for x in range(1, 6)])

