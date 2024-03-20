# Exercise 1: Declare an empty list

emptyList = []

# Exercise 2: Declare a list with more than 5 items

fiveItemList = ["There", "Is", "Five", "Items", "Here"]

# Exercise 3: Find the length of your list

print(len(fiveItemList))

# Exercise 4: Get the first item, the middle item and the last item of the list

print(fiveItemList[::2])

# Exercise 5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["John", "27", "6,5", "Not Married", "Lorem Ipsum Bvd."]

# Exercise 6: Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Exercise 7: Print the list using print()

print(it_companies)

# Exercise 8: Print the number of companies in the list

print(len(it_companies))

# Exercise 9: Print the first, middle and last company

print(it_companies[::3])

# Exercise 10: Print the list after modifying one of the companies

it_companies.pop(3)
print(it_companies)

# Exercise 11: Add an IT company to it_companies

it_companies.append("NVIDIA")
print(it_companies)

# Exercise 12: Insert an IT company in the middle of the companies list

it_companies.insert(3, "Mozilla")
print(it_companies)

# Exercise 13: Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[0] = "FACEBOOK"
print(it_companies)

# Exercise 14: Join the it_companies with a string '# '

def companyJoining(companyJoin):
    companyJoin = "# ".join(it_companies)
    print(companyJoin)

companyJoining(it_companies)

# Exercise 15: Check if a certain company exists in the it_companies list.

if "Oracle" in it_companies:
    print("This company is on the list")
else:
    print("This company isn't on the list.")

# Exercise 16: Sort the list using sort() method
    
it_companies.sort()
print(it_companies)

# Exercise 17: Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

# Exercise 18: Slice out the first 3 companies from the list

def sliceFirst(company):
    company = company[:3]
    print(company)

sliceFirst(it_companies)

# Exercise 19: Slice out the last 3 companies from the list

def sliceLast(company):
    company = company[-3:]
    print(company)

sliceLast(it_companies)

# Exercise 20: Slice out the middle IT company or companies from the list

def sliceMiddle(company):
    company = company[4::4]
    print(company)

sliceMiddle(it_companies)

# Exercise 21: Remove the first IT company from the list

it_companies.pop(0)
print(it_companies)

# Exercise 22: Remove the middle IT company from the list

it_companies.pop(3)
print(it_companies)

# Exercise 23: Remove the las IT company from the list

it_companies.pop(-1)
print(it_companies)

# Exercise 24: Remove all IT companies from the list

it_companies.clear()
print(it_companies)

# Exercise 25: Destroy the IT companies list

del it_companies

# Exercise 26: Join the following lists
#   front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#   back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

fullStack = front_end + back_end

print(fullStack)

# Exercise 27: After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

def full_stack(fullStack):
    python = "Python"
    sql = "SQL"
    indexRedux = fullStack.index("Redux") + 1
    fullStack.insert(indexRedux, python)
    indexPython = indexRedux + 1
    fullStack.insert(indexPython, sql)
    print(fullStack)


full_stack(fullStack)

# Exercise Level 2

# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()

minAge = ages[0]
maxAge = ages[-1]

print(f'The minimum age is {minAge} and the maximum is {maxAge}.')

# Add the min age and the max age again to the list

# Find the median age (one middle item or two middle items divided by two)

indexMiddleItem = round(len(ages) / 2)
medianAge = ages[indexMiddleItem] / 2

print(f'The median age is {medianAge}')

# Find the average age (sum of all items divided by their number )

sumAges = 0

for i in range (0, len(ages)):
    sumAges += ages[i] / 2

print(f'The average age is {sumAges}.')

# Find the range of the ages (max minus min)

ageRange = maxAge - minAge

print(f'The age range is {ageRange}')

# Compare the value of (min - average) and (max - average), use abs() method

minAverage = abs(minAge - sumAges)
maxAverage = abs(maxAge - sumAges)

if minAverage == maxAverage:
    print(f'Both averages are the same, being {minAverage}.')
else:
    print(f'Both averages are different, being the minAverage {minAverage} and the max average {maxAverage}.')


# Exercises Level 2: Exercise 1: Find the middle country(ies) in the countries list.

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
];

def middleCountries(countries):
    length = round(len(countries) / 2)
    print(countries[length])

middleCountries(countries)

# Exercises Level 2: Exercise 2: Divide the countries list into two equal lists if it is even if not one more country for the first half.

countriesModulus = len(countries) % 2
countriesLengthHalved = round(len(countries) / 2)

if countriesModulus == 0:
    firstHalf = countries[:countriesLengthHalved]
    secondHalf = countries[countriesLengthHalved:]
else:
    firstHalf = countries[:countriesLengthHalved + 1]
    secondHalf = countries[countriesLengthHalved:]
    print(len(secondHalf))

# Exercises Level 2: Exercises 3: ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

unpackCountries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

firstCountry, secondCountry, thirdCountry, *scandic = unpackCountries

print(firstCountry)
print(secondCountry)
print(thirdCountry)
print(scandic)