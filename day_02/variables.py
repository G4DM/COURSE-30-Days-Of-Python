# Exercises: Level 1

# Day 2: 30 Days of Python programming

firstName = "Lorem"
lastName = "Ipsum"
fullName = firstName + " " + lastName
country = "Switzerland"
city = "Zurich"
age = 33
year = 2024
is_married = False
is_true = True
is_light_on = False
firstLetter, firstNumber, euroSymbol = "A", "1", "€"

# Exercises: Level 2

# Exercise 1: Check the data type of all your variables using type() built-in function

type(firstName)
type(lastName)
type(fullName)
type(country)
type(city)
type(age)
type(year)
type(is_married )
type(is_true)
type(is_light_on)
type(firstNumber)
type(firstLetter)
type(euroSymbol)

# Exercise 2: Using the len() built-in function, find the length of your first name

len(firstName)

# Exercise 3: Compare the length of your first name and your last name

len(firstName)
len(lastName)

# Exercise 4: Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

total = num_one + num_two

diff = num_two - num_one

product = num_two * num_one

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

# Exercise 5: The radius of a circle is 30 meters.

radius = 30

area_of_circle = str(3.14 * (radius ** 2))

circum_of_circle = str((2 + 3.14) * radius)

print("Area: " + area_of_circle + " | Circumference of the circle " + circum_of_circle)

radius = int(input("Please provide an input for the radius: "))

print("Area: " + area_of_circle + " | Circumference of the circle " + circum_of_circle)

# Exercise 6: Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable namesç

firstNameInput = str(input("Please, type your first name here: "))
lastNameInput = str(input("Please, type your last name here: "))
countryInput = str(input("Please, type your country name here: "))
ageInput = int(input("Please, type your age here: "))

print(f'Your full name is {firstNameInput} {lastNameInput}, you live in {countryInput} and you are {ageInput} years old.')

help('keywords')