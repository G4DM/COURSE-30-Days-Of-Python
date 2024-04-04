# Exercises Level 1

# Exercise 1: Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

age = int(input('Please enter your age: '))

if age >= 18:
    print(f'You are old enough to drive since you are {age} years old.')
else:
    yearsLeft = 18 - age
    print(f"You can't drive yet since you are {age} years old. You need to wait {yearsLeft} years(s) until you can drive.")
    
# Exercise 2: Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age:
    age_difference = my_age - your_age
    print(f"I am {age_difference} year(s) older than you!")
elif my_age == your_age:
    print("We have the same age!")
else:
    age_difference = your_age - my_age
    print(f"You are {age_difference} year(s) older than me!")

# Exercise 3: Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 

a = float(input("Insert the first number: "))

b = float(input("Insert the second number: "))

if a > b:
    print(f"A ({a}) is greater than B ({b}).")
elif a < b:
    print(f"A ({a}) is lesser than B ({b}).")
else:
    print(f"Both A ({a}) and B ({b}) are equal!")


# Exercises Level 2

# Exercise 1: Write a code which gives grade to students according to their scores

student_grade = int(input("Please, type your grade here: "))

if 80 <= student_grade <= 100:
    print("Your score is an A. Congratulations!")
elif 70 <= student_grade <= 79:
    print("Your score is a B, close!")
elif 60 <= student_grade <=  69:
    print("Your score is a C.")
elif 50 <= student_grade <= 59:
    print("Your score is a D, be careful next time.")
elif 0 <= student_grade <= 49:
    print("Your score is F, you failed!")
else:
    print("Please type a valid grade.")

# Exercise 2: Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

user_input = input("Type out a valid month: ").lower()

if user_input == "september" or "october" or "november":
    print("The season of the month you provided is Autumn")
elif user_input == "december" or"january" or "february":
    print("The season for the month you typed is Winter.")
elif user_input == "march" or "april" or "may":
    print("The season for the month you typed is Spring.")
elif user_input == "june" or "july" or "august":
    print("The season for the month you provided is Summer.")
else:
    print("Please type a valid month.")

# Exercise 3: The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# Passing this exercise so I return later on

# Exercises Level 3

# Exercise 1: Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

middle_skill = round(len(person["skills"]) / 2)

if "skills" in person:
    print(person["skills"][middle_skill])
else:
    print("Skills key is missing.")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "skills" in person:
    if "Python" in person["skills"]:
        print("Yes, this person does have indeed the Python skills, here are all their skills:", person["skills"])
    else:
        print("This person does not have the Python skill.")
else:
    print("This person does not possess the Python skill.")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

lower_skills = person["skills"]

if "React" and "Node" and "MongoDB" in lower_skills:
    print("He is a fullstack developer.")
elif "Node" and "Python" and "MongoDB" in lower_skills:
    print("He is a backend developer.")
elif "JavaScript" and "React" in lower_skills:
    print("He is a frontend developer.")
else:
    print("He does not know enough programming languages to be a frontend, backend or fullstack developer.")

# If the person is married and if he lives in Finland, print the information in the following format:

if person["country"] == "Finland" and person["is_married"] == True:
    full_name = person["first_name"] + " " + person["last_name"]
    lives_in = "lives in Finland."
    marital_status = "is married."
    print(f'{full_name} {lives_in} He {marital_status}')