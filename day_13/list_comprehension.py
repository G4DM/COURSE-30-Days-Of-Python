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

flattened_countries = []