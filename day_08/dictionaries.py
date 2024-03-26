# Exercise 1: Create and empty dictionary called dog

dog = {}

# Exercise 2: Add name, color, breed, legs. age to the dog dictionary

dog["name"] = "Jack"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 5

print(dog)
    
# Exercise 3: Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.

student = {
    "first_name" : "Raphael",
    "last_name" : "Belluccio",
    "gender" : "male",
    "marital status" : "single",
    "skills" : ["HTML5", "CSS3", "Python", "JavaScript", "Git", "GitHub"],
    "country" : "Spain",
    "city" : "Madrid",
    "address" : {
        "zipcode" : 28001,
        "street" : "San Lucas"
    }
}

# Exercise 4: Get the length of the student dictionary

print(len(student))

# Exercise 5: Get the value of skills and check the data type, it should be a list

value = student["skills"]
dataType = type(value)

print(f'The values of skills are {value} and the type is {dataType}')

# Exercise 6: Modify the skills values by adding one or two skills

student["skills"].append("React")
student["skills"].append("Vue.js")

print(student)

# Exercise 7: Get the dictionary keys as a list

print(student.keys())

# Exercise 8: Get the dictionary values as a list

print(student.values())

# Exercise 9: Change the dictionary to a list of tuples using "items()" method

print(student.items())

# Exercise 10: Delete one of the items in the dictionary

del student["address"]

print(student)

# Exercise 11: Delete one of the dictionaries

del student