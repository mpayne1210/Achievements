# Name: task2.py
# Author: Michael Payne
# Date Created: October 02, 2022
# Date Last Modified: October 03, 2022
# Purpose: This program will display a menu of options with 3 shapes and a quit option.  It will then gather the dimensions to return the area and
#          the perimeter of the shape.  White space will be trimmed from the input.

# PSEUDOCODE:
# - Print the main menu
# - Define functions for calculations
# - Get the user to pick a shape
# - Start the loop only allowing the correct options to be selected
# - Get shape measurements in order to make calculations
# - Output results while calling the functions created at the beginning of the program, or quit if that option is chosen


# This is the creation of the starting menu
print("Geometry Calculator")
print()
print("1. Calculate the Area and Perimeter of a Square")
print("2. Calculate the Area and Perimeter of a Rectangle")
print("3. Calculate the Area and Circumference of a Circle")
print("4. Quit")
print()

# This is the creation of the functions that will be called later in the program.  These functions perform the calculations for area and perimeter.
def squareArea():
    return(squareDimension*squareDimension)
def squarePerimeter():
    return(squareDimension*4)
def rectArea():
    return(rectLength * rectWidth)
def rectPerimeter():
    return((rectLength*2) + (rectWidth*2))
def circleArea():
    return(3.14 * (radius**2))
def circleCirc():
    return((2*radius)*3.14)

# Note the strip functions here and in the rest of the program.  This is what is removing the extra space if entered by the user
shape = int(input("Enter your choice (1-4) ").strip())

# This is where the loop starts.  If a value of 1 to 4 is not selected, the user will be prompted to enter a valid option.
while not shape > 0 or not shape < 5:
    shape = int(input("please enter a valid option (1-4)").strip())

# This is the calculation for the square.  the eval('squareArea') and the like are the earlier functions being called and calculated.
if shape == 1:
    squareDimension  = float(input("Please enter the length of the sides of the square in centimeters: ").strip())
    print("The area of a square with sides" , squareDimension , "cm long is" , eval('squareArea()'), 'cm\u00b2')
    print("The perimeter of the square is " , eval('squarePerimeter()'), "cm.")

# Same as with the square but for a rectangle.
elif shape == 2:
    rectLength = float(input("Please enter the length of the rectangle in cm: ").strip())
    rectWidth = float(input("Please enter the width of the rectangle in cm: ").strip())
    print("The area of a rectangle with a length of" , rectLength , "cm and a width of" , rectWidth , "cm is" , eval('rectArea()'), 'cm\u00b2')
    print("The perimeter of the rectangle is " , eval('rectPerimeter()'), "cm.")

# Same but with a circle
elif shape == 3:
    radius = float(input("Please enter the radius of the circle in cm: ").strip())
    print("The area of a circle with a radius of" , radius , "cm is" , eval('circleArea()'), 'cm\u00b2')
    print("The circumference of the circle is " , eval('circleCirc()'), "cm.")

# Again the only other accepted option is 4 forcing the program to quit with the below message.
else:
    print("Quitting.....................")

