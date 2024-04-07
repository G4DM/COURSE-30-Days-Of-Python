# Exercises Level 1

# Exercise 1: Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(7, 6))

# Exercise 2: Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(radius):
    return 3.14 * radius * radius

print(area_of_circle(21))

# Exercise 3: Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    if type(nums) == int or float:
        for num in nums:
            total += num
        return total
    else:
        return "Only integers or float allowed."

print(add_all_nums(321,32.2,58))

# Exercise 4: Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(75))

# Exercise 5: Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    month_cap = month.capitalize()

    season = {
        "December" : "Winter",
        "January" : "Winter",
        "February" : "Winter",
        "March" : "Spring",
        "April" : "Spring",
        "May" : "Spring",
        "June" : "Summer",
        "July" : "Summer",
        "August" : "Summer",
        "September" : "Autumn",
        "October" : "Autumn",
        "November" : "Autumn",
    }

    return season[month_cap]


print(check_season("auGust"))

# Exercise 6: Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, x2, y1, y2):
    deltaY = y2 - y1
    deltaX = x2 - x1

    slope = deltaY / deltaX

    return slope

print(calculate_slope(2, 5, 6, 19))

# Exercise 7: Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):
    x_plus = (-b + (b**2 - 4 * a * c)**0.5) / 2 * a
    x_minus = (-b - (b**2 - 4 * a * c)**0.5) / 2 * a

    return "Positive way the result is", x_plus,". And the result with minus is", x_minus,"."

print(solve_quadratic_eqn(1, 2, 3))

# Exercise 8: Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(*list_to_print):
    list_to_print = list(list_to_print)
    for i in range(0, len(list_to_print), 1):
        print(list_to_print[i])

print_list("John", "Paco", "Juan")

# Exercise 9: Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(array):
    array = list(array)
    array.reverse()
    return array

print(reverse_list(["John","Paco","Juan","Nicholas"]))

# Exercise 10: Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(list_to_capitalize):
    final_list = []
    for i in range(0, len(list_to_capitalize), 1):
        indexed = list_to_capitalize[i]
        capitalized = str(indexed).capitalize()
        final_list.append(capitalized)

    return final_list
        

print(capitalize_list_items(["john","paco","juan","nicholas","staNFord"]))

# Exercise 11: Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

numbers = [2, 3, 7, 9];

def add_item(list_to_add, item):
    list_to_add.append(item)
    return list_to_add

print(add_item(food_staff, "Meat"))
print(add_item(numbers, 4))

# Exercise 12: Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(list_rm, item_to_remove):
    list_rm.remove(item_to_remove)
    return list_rm

print(remove_item(food_staff, "Mango"))
print(remove_item(numbers, 2))

# Exercise 13: Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(number):
    for i in range(0, number, 1):
        number += i
    return number

print(sum_of_numbers(10))

# Exercise 14: Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(number):
    result = 0
    for i in range(1, number + 1, 2):
        result += i

    return result

print(sum_of_odds(6))

# Exercise 15: Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(number):
    result = 0
    for i in range(0, number + 1, 2):
        result += i
    
    return result

print(sum_of_even(6))

# Exercises Level 2

# Exercise 1: Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(number):
    evens = 0
    odds = 0
    for i in range(0, number + 1, 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    result = f'The evens in {number} are {evens}, and the odds are {odds}.'

    return result

print(evens_and_odds(100))

# Exercise 2: Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(number):
    if number == 0:
        number = 1
    else:
        for i in range(1, number, 1):
            number *= i

    return number    

print(factorial(10))

# Exercise 3: Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(parameter):
    if not parameter:
        return 'Is empty'
    else:
        return 'It is not empty'

test_one = ''
test_two = 'Not empty'

print(is_empty(test_one))
print(is_empty(test_two))

# Exercise 4: Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(list_test):
    result = 0
    for i in range(0, len(list_test), 1):
        result += list_test[i]
        final_result = result / len(list_test)
    return final_result

def calculate_median(list_test):
    if len(list_test) & 2 == 0:
        even_median = 0.5 * (list_test)

list_4 = [1, 3, 6, 9, 10]

print(calculate_mean(list_4))