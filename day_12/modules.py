# region Exercises Level 1

import random
import string

# Exercise 1: Write a function which generates a six digit/character random_user_id.

def random_user_id():
    characters_id = string.digits + string.ascii_letters
    random_id = ''.join(random.choices(characters_id, k=6))

    return random_id

print(random_user_id())

# Exercise 2: Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def modified_random_user_id(characters):
    characters_id = string.digits + string.ascii_letters
    random_id = ''.join(random.choices(characters_id, k=characters))

    return random_id

def user_id_gen_by_user():
    number_of_characters = int(input("Please, type the amount of characters the ID(s) is going to have: "))
    number_of_ids = int(input("Please type the amount of ID(s) to generate: "))

    for i in range(0, number_of_ids, 1):
        print(modified_random_user_id(number_of_characters))

user_id_gen_by_user()  
    
# Exercise 3: Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    rgb_colors = []
    for i in range(0, 3, 1):
        rgb_colors.append(random.randint(0, 255))
    
    return rgb_colors

print(rgb_color_gen())

# region Exercises Level 2

# Exercise 1: Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hex_colors():
    array_characters = string.digits + string.ascii_letters

    random_array = ''.join(random.choices(array_characters, k=6))

    joined_hex = '#' + random_array

    return joined_hex

print(list_of_hex_colors())

# Exercise 2: Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():
    rgb_list = []
    for i in range(0, 3, 1):
        rgb_list.append(random.randint(0, 255))

    return rgb_list

print(list_of_rgb_colors())

# Exercise 3: Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(choice, times):
    if choice == "hexa":
        for i in range(0, times, 1):
            print('hexa:', list_of_hex_colors())
    elif choice == "rgb":
        for i in range(0, times, 1):
            print('rgb:', list_of_rgb_colors())
    else:
        return NameError

generate_colors("hexa", 5)

# region Exercises Level 3

# Exercise 1: Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(parameter):
    random.shuffle(parameter)
    return parameter

list_to_shuffle = [1, 5, 6, 2, 7, 1, 2]

print(shuffle_list(list_to_shuffle))

# Exercise 2: Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def unique_numbers():
    unique = set()
    for i in range(0, 8, 1):
        if len(unique) != 7:
            unique.add(random.randint(0, 9))
    
    return unique

print(unique_numbers())

