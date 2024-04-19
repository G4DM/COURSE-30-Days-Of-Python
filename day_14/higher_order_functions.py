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

def add_two_nums(x, y):
    return int(x) + int(y)

final = reduce(add_two_nums, numbers)

print(final)

# Exercise 4: Use for loop to print each country in the countries list.

for country in countries:
    print(country)

# I do not know if it meant the first thing, but I did it both ways

def print_list(iterable):
    print(iterable)
    return iterable

print(list(map(print_list, countries)))

# Exercise 5: Use for to print each name in the names list.

print(list(map(print_list, names)))

# Exercise 6: Use for to print each number in the numbers list.

print(list(map(print_list, numbers)))

# region Exercises Level 2

# Exercise 1: Use map to create a new list by changing each country to uppercase in the countries list

def upper_case(iterable):
    return iterable.upper()

print(list(map(upper_case, countries)))

# Exercise 2: Use map to create a new list by changing each number to its square in the numbers list

def square(iterable):
    return iterable ** 2

print(list(map(square, numbers)))

# Exercise 3: Use map to change each name to uppercase in the names list

print(list(map(upper_case, names)))

# Exercise 4: Use filter to filter out countries containing 'land'.

def filter_land(iterable):
    if "land" in iterable:
        return True
    return False

print(list(filter(filter_land, countries)))

# Exercise 5: Use filter to filter out countries having exactly six characters.

def filter_six(iterable):
    if len(iterable) != 6:
        return True
    return False

print(list(filter(filter_six, countries)))

# Exercise 6: Use filter to filter out countries containing six letters and more in the country list.

def filter_six_or_more(iterable):
    if len(iterable) <= 6:
        return True
    return False

print(list(filter(filter_six_or_more, countries)))

# Exercise 7: Use filter to filter out countries starting with an 'E'

def filter_e(iterable):
    lower_case = iterable.lower()
    if "e" in lower_case[0]:
        return False
    return True

print(list(filter(filter_e, countries)))