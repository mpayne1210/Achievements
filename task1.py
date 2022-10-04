# Name: task1.py
# Author: Michael Payne
# Date Created: October 02, 2022
# Date Last Modified: October 03, 2022
# Purpose: This is a Geometry Calculator.  This program will display a menu wil 3 shapes and a quit option.  It will then calculate the
#          area and perimeter of the shape and provide the results.  

# This part is just displaying the menu
print("Geometry Calculator")
print()
print("1. Calculate the Area of a Cirlce")
print("2. Calculate the Area of a Rectangle")
print("3. Calculate the Area of a Right-Angle Triange")
print("4. Quit")
print()

shape = int(input("Enter your choice (1-4) "))

# This is where the loop is created forcing an answer between 1 and 4
while not shape > 0 or not shape < 5:
    shape = int(input("please enter a valid option (1-4)"))

# This calculates the area and perimeter (circumference) of the circle.  The calculations are done within the print statement keeping code short 
# and simple.  See the end of the first print line calculation - that is how the cm squared gets displayed in python as you will see in the output.
# The calculation for the radius of a circle is pi times the radius squared.  The circumference is pi times twice the radius
if shape == 1:
    radius = float(input("Please enter the radius of the circle in cm: "))
    print("The area of a circle with a radius of" , radius , "cm is", 3.14 * radius ** 2 , 'cm\u00b2')
    print("The Circumference of the circle is" , (2 * radius) * 3.14 , "cm.")

# This calculates the are and perimeter of the rectangle and the calulations are done just as with the circle.  The formula for the area of a square of rectange
# is length times width.  The area is twice the width plus twice the length.  
elif shape == 2:
    rectangleWidth = float(input("Please enter the width of the rectangle in cm: "))
    rectangleLength = float(input("Please enter the length of the rectangle in cm: "))
    print("The area of a rectangle " , rectangleWidth , "cm wide and " , rectangleLength , "cm long is ", rectangleLength * rectangleWidth , 'cm\u00b2')
    print("The Perimeter is " , 2 * rectangleWidth + 2 * rectangleLength , "cm")

# This of course calculates the Triangle.  Only a right angle triangle is supported as otherwise we would need to know an angle or the length of the other side
# to know the type of triangle in order to calculate the correct area.  2 triangles with 2 sides the same can have different areas depending on the angles involved.
# In order to calculate the perimeter, we still needed to calculate the third side which is why hypotenuse was delcated as a variable.
elif shape == 3:
    triangleHeight = float(input("Please enter the triangle height in cm: "))
    triangleLength = float(input("Please enter the triangle length in cm: "))
    hypotenuse = (triangleHeight ** 2 + triangleLength ** 2) ** 0.5
    print("The area of a triangle " , (triangleHeight * triangleLength) /2 , 'cm\u00b2')
    print("The perimeter is " , hypotenuse + triangleLength + triangleHeight , "cm.")

# The end of the program.  Since the loop only allows options between 1 and 4, this is the only possibility left.
else:
    print("Quitting...................")




