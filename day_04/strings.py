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

variableExercise12 = "Python for Everyone"

print(variableExercise12.replace("Everyone", "All"))

# Exercise  13: Split the string 'Coding For All' using space as the separator (split()) .

print(company.split(" "))

# Exercise  14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

faang = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(faang.split(", "))

# Exercise  15: What is the character at index 0 in the string Coding For All.

print(company[0])

# Exercise  16: What is the last index of the string Coding For All.

print(company[-1])

# Exercise  17: What character is at index 10 in "Coding For All" string.

print(company[10])

# Exercise  18: Create an acronym or an abbreviation for the name 'Python For Everyone'.

def acronymAbbreviation(text):
    text = text.split(" ")
    firstWord = text[0]
    secondWord = text[1]
    thirdWord = text[2]
    print(firstWord[0] + secondWord[0] + thirdWord[0])

variablePFE = "Python For Everyone"

acronymAbbreviation(variablePFE)

# Exercise  19: Create an acronym or an abbreviation for the name 'Coding For All'.

company = "Coding For All"

acronymAbbreviation(company)

# Exercise  20: Use index to determine the position of the first occurrence of C in Coding For All.

print(company.index("C"))

# Exercise  21: Use index to determine the position of the first occurrence of F in Coding For All.

print(company.index("F"))

# Exercise  22: Use rfind to determine the position of the last occurrence of l in Coding For All People.

codingForAllPeople = company + " People"

print(codingForAllPeople.rfind("l"))

# Exercise  23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

textSentence = "You cannot end a sentence with because because because is a conjunction"

print(f'The position of the first occurrence of the word "because" with "find" is: {textSentence.find("because")}')

print(f'The position of the first occurrence of the word "because" with "index" is: {textSentence.index("because")}')

# Exercise  24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(f'The position of the last occurrence of the word "because" with "rindex" is: {textSentence.rindex("because")}')

# Exercise  25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(f'The result of slicing "because because because" from the sentence is: {textSentence.replace("because ", "")}')

# [This exercise is the same as the 23th one] Exercise  26: Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# [This exercise is duplicated, see 25th] Exercise  27: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# Exercise  28: Does ''Coding For All' start with a substring Coding?

def startsWith(text):
    text = text.split(" ")
    firstWord = text[0]
    if firstWord == "Coding":
        print("Yes, it does start with a substring 'Coding'")
    else:
        print("Try again.")

startsWith(company)

# Exercise  29: Does 'Coding For All' end with a substring coding?

def endsWith(text):
    text = text.split(" ")
    lastWord = text[-1]
    if lastWord == 'coding':
        print("Try again.")
    else:
        print("It does not end with 'coding'")

endsWith(company)

# Exercise  30: '   Coding For All      '  , remove the left and right trailing spaces in the given string.

variableLeftRight = '   Coding For All      '

print(variableLeftRight.replace("   ", ""))

# Exercise  31: Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python

variable30DOP = "30DaysOfPython"
variableTDOP = "thirty_days_of_python"

print(f'The first variable returned: {variable30DOP.isidentifier()}')
print(f'The second variable returned: {variableTDOP.isidentifier()}')

# Exercise  32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

listExercise32 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print("# ".join(listExercise32))

# Exercise  33: Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.

lineEscape = "I am enjoying this challenge.\nI just wonder what is next."

print(lineEscape)

# Exercise  34: Use a tab escape sequence to write the following lines.
#   Name      Age     Country   City
#   Asabeneh  250     Finland   Helsinki

tabEscape = "Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"

print(tabEscape)

# Exercise  35: Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
formattedString = f'The area of a circle with radius {radius} is {area} meters square'

print(formattedString)

# Exercise  36: Make the following using string formatting methods:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144

num1 = 8
num2 = 6

addition = num1 + num2
difference = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
floorDivision = num1 // num2
exponentiation = num1 ** num2

print(f'The result of {num1} + {num2} = {addition}')
print(f'The result of {num1} - {num2} = {difference}')
print(f'The result of {num1} * {num2} = {multiplication}')
print(f'The result of {num1} / {num2} = {division}')
print(f'The result of {num1} % {num2} = {modulus}')
print(f'The result of {num1} // {num2} = {floorDivision}')
print(f'The result of {num1} ** {num2} = {exponentiation}')



