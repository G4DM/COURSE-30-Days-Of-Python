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

