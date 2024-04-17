# region Exercises Level 1

# Exercise 1: Explain the difference between map, filter, and reduce.

"""
Map applies a function to each iterable item.
Filter basically filters items from an iterable.
Reduce reduces the item sequency to a single value.
"""

# Exercise 2: Explain the difference between higher order function, closure and decorator

"""
Higher Order Functions are functions that can take other functions as arguments and/or return functions as results.
Closures are functions that capture variables from their enclosing scope and retain access to these variables even after the outer function has finished executing.
Decorators are functions that modify/Extend the behavior of other functions without modifying their internal code.
"""

# Exercise 3: Define a call function before map, filter or reduce, see examples.

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map

def cubic(x):
    return x ** 3

numbers_cubic = map(cubic, numbers)

print(list(numbers_cubic))

# filter

def is_odd(num):
    if num % 2 == 0:
        return False
    return True

odd_numbers = filter(is_odd, numbers)

print(list(odd_numbers))

# reduce

def reduce_countries(x):
    return x

final = reduce(reduce_countries, countries)

print(final)