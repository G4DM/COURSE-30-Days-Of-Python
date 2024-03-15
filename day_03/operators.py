# Exercise 1: Declare your age as integer variable

myAge = 20

# Exercise 2: Declare your height as a float variable

myHeight = 6.1

# Exercise 3: Declare a variable that store a complex number

complexNumber = 3j

# Exercise 4: Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

def baseHeightTriangle():
    baseTriangle = float(input("Please, provide a base for the Triangle: "))
    heightTriangle = float(input("Please, provide a height for the triangle: "))
    areaTriangle = 0.5 * baseTriangle * heightTriangle
    print(f'The total area of the triangle given the answers provided is: {areaTriangle}')

baseHeightTriangle()

# Exercise 5: Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

def threeSideTriangle():
    aSideTriangle = float(input("Please, provide a number for the A side of the triangle: "))
    bSideTriangle = float(input("Please, provide a number for the B side of the triangle: "))
    cSideTriangle = float(input("Please, provide a number for the C side of the triangle: "))
    perimeterTriangle = aSideTriangle + bSideTriangle + cSideTriangle
    print(f'The total perimeter of the triangle given the provided answers is: {perimeterTriangle}')

threeSideTriangle()

# Exercise 6: Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

def rectangleQuestion():
    rectangleLength = float(input("Please, type a length for the rectangle: "))
    rectangleHeight = float(input("Please, type a height for the rectangle: "))
    rectangleArea = rectangleLength * rectangleHeight
    rectanglePerimeter = 2 * (rectangleLength + rectangleHeight)
    print(f'The area of the rectangle applying the answers given is: {rectangleArea} and its perimeter is {rectanglePerimeter}')

rectangleQuestion()

# Exercise 7: Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

def circleQuestion():
    radiusCircle = float(input("Please, provide a Circle Radius to begin with: "))
    circleArea = 3.14 * radiusCircle * radiusCircle
    circleCircumference = 2 * 3.14 * radiusCircle
    print(f'Given the provided radius, the area is {circleArea} and the circumference is {circleCircumference}')

circleQuestion()



# Exercise 8: Calculate the slope, x-intercept and y-intercept of y = 2x -2



# Exercise 9: Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)



# Exercise 10: Compare the slopes in tasks 8 and 9.



# Exercise 11: Calculate the value of y (y = x**2 + 6 * x + 9). Try to use different X values and figure out at what X value Y is going to be 0.

def ex11(x):
    y = x ** 2 + 6 * x + 9
    print(y)

ex11(0)
ex11(5)
ex11(10)

# Exercise 12: Find the length of 'python' and 'dragon' and make a falsy comparison statement.

pythonName = "python"
dragonName = "dragon"

if len(pythonName) != len(dragonName):
    print("The falsy comparison went wrong!")
else:
    print("Nice! The falsy comparison worked!")

# Exercise 13: Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'.

if "on" in pythonName and dragonName:
    print("Yes, it worked! Both contain 'on'!")
else:
    print("Try again! It did not work :(")

# Exercise 14: 'I hope this course is not full of jargon'. Use 'in' operator to check if 'jargon' is in the sentence.

testEx14 = "I hope this course is not full of jargon"

if "jargon" in testEx14:
    print("Well done! It contained the word 'jargon'!")
else:
    print("Try again!")