# Exercise 1: Declare your age as integer variable

myAge = 20

# Exercise 2: Declare your height as a float variable

myHeight = 6.1

# Exercise 3: Declare a variable that store a complex number

complexNumber = 3j

# Exercise 4: Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

baseTriangle = float(input("Please, provide a base for the Triangle: "))
heightTriangle = float(input("Please, provide a height for the triangle: "))
areaTriangle = 0.5 * baseTriangle * heightTriangle

print(f'The total area of the triangle given the answers provided is: {areaTriangle}')

# Exercise 5: Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

aSideTriangle = float(input("Please, provide a number for the A side of the triangle: "))
bSideTriangle = float(input("Please, provide a number for the B side of the triangle: "))
cSideTriangle = float(input("Please, provide a number for the C side of the triangle: "))
perimeterTriangle = aSideTriangle + bSideTriangle + cSideTriangle

print(f'The total perimeter of the triangle given the provided answers is: {perimeterTriangle}')

# Exercise 6: Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

rectangleLength = float(input("Please, type a length for the rectangle: "))
rectangleHeight = float(input("Please, type a height for the rectangle: "))
rectangleArea = rectangleLength * rectangleHeight
rectanglePerimeter = 2 * (rectangleLength + rectangleHeight)

print(f'The area of the rectangle applying the answers given is: {rectangleArea} and its perimeter is {rectanglePerimeter}')

# Exercise 7: Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radiusCircle = float(input("Please, provide a Circle Radius to begin with: "))
circleArea = 3.14 * radiusCircle * radiusCircle
circleCircumference = 2 * 3.14 * radiusCircle

print(f'Given the provided radius, the area is {circleArea} and the circumference is {circleCircumference}')

# Exercise 8: Calculate the slope, x-intercept and y-intercept of y = 2x -2