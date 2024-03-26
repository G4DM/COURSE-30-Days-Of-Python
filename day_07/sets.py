# Exerices: Level 1

# Exercise 1: Find the length of the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))

# Exercise 2: Add 'Twitter' to it_companies

twitter = {'Twitter'}
it_companies.update(twitter)

print(it_companies)

# Exercise 3: Insert multiple IT companies at once to the set it_companies

multipleCompanies = {'BenQ', 'HP', 'Logitech', 'Dell', 'Asus'}
it_companies.update(multipleCompanies)

print(it_companies)

# Exercise 4: Remove one of the companies from the set it_comapnies

it_companies.pop()

print(it_companies)

# Exercise 5: What is the difference between remove and discard

# If the "remove" attribute doesn't find any coincidences, it will raise errors, while "discard" will not.

# Exercises: Level 2

# Exercise 1: Join A and B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

print(C)

# Exercise 2: Find A intersection B

print(A.intersection(B))

# Exercise 3: Is A subset of B

print(A.issubset(B))

# Exercise 4: Are A and B disjoint sets

print(A.isdisjoint(B))

# Exercise 5: Join A with B and B with A

aWithB = A.union(B)
bWithA = B.union(A)

print(aWithB)
print(bWithA)

# Exercise 6: What is the symmetric difference between A and B

print(A.symmetric_difference(B))

# Exercise 7: Delete the sets completely

del A
del B

# Exercises: Level 3

# Exercise 1: Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age))

age = set(age)
print(len(age))

# len(list) > len(set)

# Exercise 2: Explain the difference between the following data types: string, list, tuple and set.

# String: Collection of words.
# List: Stored in a variable and can contain "multiple string together". It is mutable.
# Tuple: Same as a list but it is immutable.
# Set: Same as the set, but once created, cannot be changed.

# Exercise 3: "I am a teacher and I love to inspire and teach people." How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

text = {'I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and','teach','people'}

print("There are", len(text), "unique words in the text.")