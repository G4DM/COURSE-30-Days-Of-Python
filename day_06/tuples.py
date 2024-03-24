# Exercise 1: Create an empty tuple

emptyTuple = ()
emptyTupleV2 = tuple()

# Exercise 2: Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ('John', 'Alex', 'Robert')
sisters = ('Marla', 'Maria', 'Marta')

# Exercise 3: Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters

# Exercise 4: How many siblings do you have?

print('I have',  len(siblings), 'siblings.')

# Exercise 5: Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parents = ('Francesca', 'Constantin')

family_members = siblings + parents

print(family_members)

# Exercises Level 2: Exercise 1: Unpack siblings and parents from family_members

unpackedSiblings = family_members[:-2]
unpackedParents = family_members[-2:]

# Exercises Level 2: Exercise 2: Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Apple', 'Pear', 'Banana')
vegetables = ('Onion', 'Bell Pepper', 'Lettuce')
animalProducts = ('Chicken Breast', 'Chicken Thigh', "Lamb Chop")

food_stuff_tp = fruits + vegetables + animalProducts

# Exercises Level 2: Exercise 3: Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Exercises Level 2: Exercise 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

def sliceOut(lst):
    halvedLength = round(len(lst) / 2)
    lst.pop(halvedLength)
    print(lst)

sliceOut(food_stuff_lt)

# Exercises Level 2: Exercise 5: Slice out the first three items and the last three items from food_staff_lt list

def sliced(lst):
    for i in range(0, 3):
        i += 1
        lst.pop(1)
    print(lst )
    for i in range(-3, 0):
        lst.pop(i)
    print(lst)

sliced(food_stuff_lt)


# Exercises Level 2: Exercise 6: Delete the food_staff_tp tuple completely

del food_stuff_tp

# Exercises Level 2: Exercise 7: Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country

if 'Estonia' in nordic_countries:
    print("Yes, Estonia it is a nordic country.")
else:
    print("No, Estonia it is not a nordic country.")

# Check if 'Iceland' is a nordic country
    
if 'Iceland' in nordic_countries:
    print("Yes, Iceland is a nordic country.")
else:
    print("No, Iceland it is not a nordic country.")