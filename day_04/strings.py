# Exercise 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

def exercise1():
    Thirty = "Thirty"
    Days = "Days"
    Of = "Of"
    Python = "Python"
    space = " "

    stringsConcatenation = Thirty + space + Days + space + Of + space + Python

    print(stringsConcatenation)

exercise1()

# Exercise 2: Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

Coding = "Coding"
For = "For"
All = "All"
space = " "

concatenation = Coding + space + For + space + All

print(concatenation)

# Exercise 3: Declare a variable named company and assign it to an initial value "Coding For All".

company = concatenation

# Exercise 4: Print the variable company using print().

print(company)

# Exercise 5: Print the length of the company string using len() method and print().


print(len(company))

# Exercise 6: Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Exercise 7: Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Exercise 8: Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Exercise 9: Cut(slice) out the first word of Coding For All string.

print(company[1:])

# Exercise  10: Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.index("Coding"))
print(company.find("Coding"))

if "Coding" in company:
    print("Yes! The word 'Coding' is inside the 'company' variable.")
else:
    print("Are you sure?")

# Exercise  11: Replace the word coding in the string 'Coding For All' to Python.
    
def exercise11():
    lowerCaseCompany = company.lower()
    print(lowerCaseCompany.replace("coding", "python").title())

exercise11()

# Exercise  12: Change Python for Everyone to Python for All using the replace method or other methods.



# Exercise  13: Split the string 'Coding For All' using space as the separator (split()) .
# Exercise  14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# Exercise  15: What is the character at index 0 in the string Coding For All.
# Exercise  16: What is the last index of the string Coding For All.
# Exercise  17: What character is at index 10 in "Coding For All" string.
# Exercise  18: Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Exercise  19: Create an acronym or an abbreviation for the name 'Coding For All'.
# Exercise  20: Use index to determine the position of the first occurrence of C in Coding For All.
# Exercise  21: Use index to determine the position of the first occurrence of F in Coding For All.
# Exercise  22: Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Exercise  23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Exercise  24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Exercise  25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Exercise  26: Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Exercise  27: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Exercise  28: Does ''Coding For All' start with a substring Coding?
# Exercise  29: Does 'Coding For All' end with a substring coding?
# Exercise  30: '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Exercise  31: Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python

# Exercise  32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Exercise  33: Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
# Exercise  34: Use a tab escape sequence to write the following lines.
#   Name      Age     Country   City
#   Asabeneh  250     Finland   Helsinki
# Exercise  35: Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
# Exercise  36: Make the following using string formatting methods:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144
