# region Exercises Level 1

# Exercise 1: Explain the difference between map, filter, and reduce.

"""
Map applies a function to each iterable item.
Filter basically filters items from an iterable.
Reduce reduces the item sequency to a single value.
"""

# Exercise 2: Explain the difference between higher order function, closure and decorator

"""
Higher Order Functions are functions that can take other functions as arguments and/or return functions as results.
Closures are functions that capture variables from their enclosing scope and retain access to these variables even after the outer function has finished executing.
Decorators are functions that modify/Extend the behavior of other functions without modifying their internal code.
"""

# Exercise 3: Define a call function before map, filter or reduce, see examples.

from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map

def cubic(x):
    return x ** 3

numbers_cubic = map(cubic, numbers)

print(list(numbers_cubic))

# filter

def is_odd(num):
    if num % 2 == 0:
        return False
    return True

odd_numbers = filter(is_odd, numbers)

print(list(odd_numbers))

# reduce

def add_two_nums(x, y):
    return int(x) + int(y)

final = reduce(add_two_nums, numbers)

print(final)

# Exercise 4: Use for loop to print each country in the countries list.

for country in countries:
    print(country)

# I do not know if it meant the first thing, but I did it both ways

def print_list(iterable):
    print(iterable)
    return iterable

print(list(map(print_list, countries)))

# Exercise 5: Use for to print each name in the names list.

print(list(map(print_list, names)))

# Exercise 6: Use for to print each number in the numbers list.

print(list(map(print_list, numbers)))

# region Exercises Level 2

# Exercise 1: Use map to create a new list by changing each country to uppercase in the countries list

def upper_case(iterable):
    return iterable.upper()

print(list(map(upper_case, countries)))

# Exercise 2: Use map to create a new list by changing each number to its square in the numbers list

def square(iterable):
    return iterable ** 2

print(list(map(square, numbers)))

# Exercise 3: Use map to change each name to uppercase in the names list

print(list(map(upper_case, names)))

# Exercise 4: Use filter to filter out countries containing 'land'.

def filter_land(iterable):
    if "land" in iterable:
        return True
    return False

print(list(filter(filter_land, countries)))

# Exercise 5: Use filter to filter out countries having exactly six characters.

def filter_six(iterable):
    if len(iterable) != 6:
        return True
    return False

print(list(filter(filter_six, countries)))

# Exercise 6: Use filter to filter out countries containing six letters and more in the country list.

def filter_six_or_more(iterable):
    if len(iterable) <= 6:
        return True
    return False

print(list(filter(filter_six_or_more, countries)))

# Exercise 7: Use filter to filter out countries starting with an 'E'

def filter_e(iterable):
    lower_case = iterable.lower()
    if "e" in lower_case[0]:
        return False
    return True

print(list(filter(filter_e, countries)))

# Exercise 8: Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))

print(result)

# Exercise 9: Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

test_list = [1, 2, "Hello", 3, "4"]

def get_string_lists(parameter):
    if isinstance(parameter, str) == True:
        return True
    return False

print(list(filter(get_string_lists, test_list)))

# Exercise 10: Use reduce to sum all the numbers in the numbers list.

def sum_all(x, y):
    return int(x) + int(y)

print(reduce(sum_all, numbers))

# Exercise 11: Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

countries_sentence = reduce(lambda x, y: f"{x}, {y}", countries)

print(f'{countries_sentence} are north European countries.')

# Exercise 12: Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

def common_pattern(iterable):
    if "ia" in iterable:
        return True
    return False

print(list(filter(common_pattern, countries)))

# Exercise 13: Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

def countries_dict(iterable):
    new_dict = {}
    for i in range(len(iterable)):
        first_letter = iterable[i][0]
        new_dict[first_letter] = new_dict.get(first_letter, 0) + 1
    return new_dict

print(dict(map(countries_dict, countries)))