# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for class, files, tool windows, actions, and settings.
from utility import util
from classes.Celsius import Celsius
from functools import reduce
from itertools import count
import math
import random
import os
import re

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
greet_user = lambda name6: print('Hey there,', name6)
upgrade = lambda self, value8, args, offset=0, limit=None, order=None, count2=False: value8 if count2 else self.browse(
    value8)
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
tuple1 = ('Hello',)
greet = 'Python is fun'
print(greet.upper())
print(greet.partition('is '))
print(greet.replace('H', 'T'))
print(greet.startswith('T'))
print(greet.isnumeric())
print(greet.index('y'))
# escape double quotes
example = "He said, \"What's there?\""
# escape single quotes
example1 = 'He said, "What\'s there?"'
print(example)
print(example1)

# Escape Sequence	Description
# \\	            Backslash
# \'	            Single quote
# \"	            Double quote
# \a	            ASCII Bell
# \b	            ASCII Backspace
# \f	            ASCII Form feed
# \n	            ASCII Linefeed
# \r	            ASCII Carriage Return
# \t	            ASCII Horizontal Tab
# \v	            ASCII Vertical Tab
# \ooo	            Character with octal value ooo
# \xHH	            Character with hexadecimal value HH
name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}')
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)
# using add() method
numbers.add(32)
print('Updated Set:', numbers)
# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc).
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)
# first set
A = {1, 3, 5}
print(' A set is contain :', A)
# second set
B = {0, 2, 4}
print(' B set is contain :', B)
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B))
# perform intersection operation using &
print('Intersection using &:', A & B)
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))
# perform difference operation using &
print('Difference using &:', A - B)
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))
# try:
#     textFile = open("/home/mehrdad/Desktop/4444.txt", "r")
#     readContent = textFile.read()
#     print(readContent)
# finally:
#     textFile.close()

with open("/home/mehrdad/Desktop/4444.txt", "r") as textFileRead:
    readContent = textFileRead.read(500)
    print(readContent)
    with open("/home/mehrdad/Desktop/4444.txt", "w") as textFileWrite:
        textFileWrite.write(readContent)
# getcwd() returns the current directory in the form of a string.
print(os.getcwd())
# chdir() method to change the current working directory and passed a new path as a string to chdir()
os.chdir('/home/mehrdad/PycharmProjects/test/')
print(os.getcwd())
print(os.listdir())
print(os.listdir('/home/mehrdad/PycharmProjects/'))
# delete "mydir" directory and all of its contents
# shutil.rmtree("mydir")
# view all the built-in exceptions using the built-in local() function
print(dir(locals()['__builtins__']))

# AssertionError	    Raised when an assert statement fails.
# AttributeError	    Raised when attribute assignment or reference fails.
# EOFError	            Raised when the input() function hits end-of-file condition.
# FloatingPointError	Raised when a floating point operation fails.
# GeneratorExit	        Raise when a generator's close() method is called.
# ImportError	        Raised when the imported module is not found.
# IndexError	        Raised when the index of a sequence is out of range.
# KeyError	            Raised when a key is not found in a dictionary.
# KeyboardInterrupt	    Raised when the user hits the interrupt key (Ctrl+C or Delete).
# MemoryError	        Raised when an operation runs out of memory.
# NameError	            Raised when a variable is not found in local or global scope.
# NotImplementedError	Raised by abstract methods.
# OSError	            Raised when system operation causes system related error.
# OverflowError	        Raised when the result of an arithmetic operation is too large to be represented.
# ReferenceError	    Raised when a weak reference proxy is used to access a garbage collected referent.
# RuntimeError	        Raised when an error does not fall under any other category.
# StopIteration	        Raised by next() function to indicate that there is no further item to be returned by iterator.
# SyntaxError	        Raised by parser when syntax error is encountered.
# IndentationError	    Raised when there is incorrect indentation.
# TabError	            Raised when indentation consists of inconsistent tabs and spaces.
# SystemError	        Raised when interpreter detects internal error.
# SystemExit	        Raised by sys.exit() function.
# TypeError	            Raised when a function or operation is applied to an object of incorrect type.
# UnboundLocalError	    Raised when a reference is made to a local variable in a
#                       function or method, but no value has been bound to that variable.
# UnicodeError	        Raised when a Unicode-related encoding or decoding error occurs.
# UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
# UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
# UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
# ValueError	        Raised when a function gets an argument of correct type but improper value.
# ZeroDivisionError	    Raised when the second operand of division or modulo operation is zero.
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(reciprocal)
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except ZeroDivisionError:
    print("Error: Denominator cannot be 0.")

finally:
    print("This is finally block.")
no_of_sides = 4
my_list0 = [i for i in range(10)]
my_list1 = [i * 2 for i in range(10)]
my_list2 = [i * 2 for i in range(10) if i % 2 == 0]
my_list3 = [i * 2 if i % 2 == 0 else i for i in range(10)]
my_list4 = [i * j for i in range(4) for j in range(4)]
my_list5 = [[i * j for j in range(4)] for i in range(4)]
my_list6 = sides = [0 for i in range(no_of_sides)]
print(my_list6)

# define a list
my_list = [4, 7, 0]
# create an iterator from the list
iterator = iter(my_list)
# get the first element of the iterator
print(next(iterator))  # prints 4
# get the second element of the iterator
print(next(iterator))  # prints 7
# get the third element of the iterator
print(next(iterator))  # prints 0
# create a list of integers
my_list = [1, 2, 3, 4, 5]
# create an iterator from the list
iterator = iter(my_list)
# iterate through the elements of the iterator
for element in iterator:
    # Print each element
    print(element)

# create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)

# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))


# Python Generator
def my_generator(n):
    # initialize counter
    valueGenerator = 0
    # loop until counter is less than n
    while valueGenerator < n:
        # produce the current value of the counter
        yield valueGenerator
        # increment the counter
        valueGenerator += 1


# iterate over the generator object produced by my_generator
for value in my_generator(3):
    # print each value produced by generator
    print(value)

# We can also create a generator object from the generator function by calling the function
# like we would any other function as:
generator = my_generator(3)
print(next(generator))  # 0
print(next(generator))  # 1
print(next(generator))  # 2
# Python Generator Expression
# Generator Expression Syntax is
# (expression for item in iterable)
# create the generator object
squares_generator = (i * i for i in range(5))
# iterate over the generator and print the values
for i in squares_generator:
    print(i)


def PowTwoGen(maxNumber=0):
    n = 0
    while n < maxNumber:
        yield 2 ** n
        n += 1


# Generator for Represent Infinite Stream
def all_even():
    n = 0
    while True:
        yield n
        n += 2


# Pipelining Generators
# Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.
def fibonacci_numbers(nums):
    x5, y5 = 0, 1
    # If we do not intend to use items of a sequence within the loop, we can write the loop like this:
    for _ in range(nums):
        x5, y5 = y5, x5 + y5
        yield x5


def square(nums):
    for num1 in nums:
        yield num1 ** 2


print(sum(square(fibonacci_numbers(10))))


# Nested function in Python
def greet(name1):
    # inner function
    def display_name():
        print("Hi", name1)

    # call inner function
    display_name()


# call outer function
greet("John")


# Python Closures
# All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function.
# The closure is a nested function that helps us access the outer
# function's variables even after the external function is closed.
def greet():
    # variable defined outside the inner function
    name2 = "John"

    # return a nested anonymous function
    return lambda: "Hi " + name2


# call the outer function
message = greet()

# call the inner function
print(message())


# Output: Hi John

def calculate():
    num3 = 1

    def inner_func():
        nonlocal num3
        num3 += 2
        return num3

    return inner_func


# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())


# Pass Function as Argument
def add(x4, y4):
    return x4 + y4


def calculate(func, x5, y5):
    return func(x5, y5)


result = calculate(add, 4, 6)
print(result)  # prints 10


# Return a Function as a Value
def greeting(name4):
    def hello():
        return "Hello, " + name4 + "!"

    return hello


greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"


# Output: Hello, Atlantis!

# Python Decorators
def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")
        # call original function
        func()

    # return the inner function
    return inner


# define ordinary function
@make_pretty
def ordinary():
    print("I am ordinary")


# decorate the ordinary function
# make_pretty() is a decorator.
decorated_func = make_pretty(ordinary)
# call the decorated function
decorated_func()
# Instead of assigning the function call to a variable,
# Python provides a much more elegant way to achieve this functionality using the @ symbol.
# Now call decorator like below
# Here, the ordinary() function is decorated with the make_pretty() decorator
# using the @make_pretty syntax, which is equivalent to calling ordinary = make_pretty(ordinary).
ordinary()


# Decorating Functions with Parameters
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(2, 5)
divide(2, 0)


# Chaining Decorators in Python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

# create an object
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
# coldest_thing = Celsius(-300)


pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")


