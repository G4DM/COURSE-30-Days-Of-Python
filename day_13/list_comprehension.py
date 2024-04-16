# Exercise 1: Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered = [i for i in range(numbers[0], numbers[-1], 1) if i <= 0]

print(filtered)

# Exercise 2: Flatten the following list of lists of lists to a one dimensional list :

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

dimensional = [number for row in list_of_lists for number in row]
flattened = [number for row in dimensional for number in row]

print(flattened)

# Exercise 3: Using list comprehension create the following list of tuples:

numbers = [i ** k for i in range(0, 10, 1) for k in range(0, 6, 1)]

print(numbers)

# Exercise 4: Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]

print(flattened_countries)

# Exercise 5: Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dictionary_countries = {}

exercise_5 = [{"country": country.upper(), "capital": capital.upper()} for sublist in countries for country, capital in sublist]

print(exercise_5)

# Exercise 6: Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

exercise_6 = [name + " " + surname for sublist in names for name, surname in sublist]

print(exercise_6)

# Exercise 7: Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

print(slope(2, 4, 5, 10))