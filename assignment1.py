# Name: assignment1.py
# Author: Michael Payne
# Date Created: October 04, 2022
# Date Last Modified: October 09, 2022
# Purpose: The purpose of this program is to provide a customer a menu of 2 items to order for delivery from an expanding restaurant.  It will require 
#          taking the customer information, providing the menu, taking the order, confirming if the order is correct, calculating the total and applying
#          a discount based on the amount of the order, providing a further discount if the customer claims to be a student, calculating tax, and providing a receipt.
#          The program will only accept valid input and removes blank spaces.  It will accept either capital or lower case answers.  I have figured out how to 
#          include additional features which will be explained in the inline comments.  Enjoy!

# Welcome Message
print("Welcome to Arnold's Amazing Eats II.  We are expanding our amazing services, and offering the best food in Waterloo delivered \
straight to your door! \nFor now, you can pick any quantity of either of our 2 fantastic selections, however we will be expanding \
our menu soon. \nTo place an order please follow the instructions: ")
print()
print()
print("First, let me get some information to start your order.  Please enter the following details:")

# Taking customer information.  Using bool blank input will not be accepted unless it is for the unity number which is optional.  The 
# .strip() will remove any blank spaces from the input.
firstName = input("First Name: ").strip()
while bool(firstName) == False:
    firstName = input("First Name: ").strip()
lastName = input("Last Name: ").strip()
while bool(lastName) == False:
    lastName = input("Last Name: ").strip()
streetNumber = input("Street Number: ").strip()
while bool(streetNumber) == False:
    streetNumber = input("Street Number: ").strip()
streetName = input("Street Name: ").strip()
while bool(streetName) == False:
    streetName = input("Street Name: ").strip()
unitNumber = input("Unit Number (Leave blank if empty: ")
city = input("City: ").strip()
while bool(city) == False:
    city = input("City: ").strip()
province = input("Province: ").strip()
while bool(province) == False:
    province = input("Province: ").strip()
postalCode = input("Postal Code: ").strip()
while bool(postalCode) == False:
    postalCode = input("Postal Code: ").strip()
print()
specialNotes = input("If you have any special instructions for deliveries to this address, please enter them here: ").strip()

print()

# This is presenting the menu using a list format.  It is using a loop so that later in the program if the customer wants to change what they 
# ordered at the confirmation screen they will return here to select a new option.
while True:
    print("Please select your desired option from the following menu.")
    print()
    menuList = ["1) Burnt Pizza With Donkey Guts     $150" ,  "2) Melted Ice With Frozen Water     $75"]
    for x in menuList:
        print(x)
    print()

    # This is asking for the selection and storing the selction in the variable called menuChoice.  only 1 or 2 will be accepted and blank space is removed
    # from the input using .strip().
    menuChoice = input("Please select 1 or 2: ").strip()
    while  menuChoice != "1" and menuChoice != "2":
        menuChoice = input("please enter a selection. (Type 1 or 2): ").strip()  

    # This assigns a price of either $150 or $75 depending option is selected, and tells the program what the order is
    if menuChoice == "1":
        selection = "Burnt Pizza With Donkey Guts"
        price = 150
    else:
        selection = "Melted Ice With Frozen Water"
        price = 75

    # This part is what I figured out will format the numbers in the form of currency. (adds a dollar sign and rounds to 2 decimal places. :)
    formatprice = "${:,.2f}".format(price)          
    print()

    # Asking for the quantity of items.  This will not accept a blank input and will only accept numbers :)
    servingQuantity = input("Excellent! How many servings would you like?").strip()
    while bool(servingQuantity) == False or servingQuantity.isnumeric() == False:
        servingQuantity = (input("Please enter a valid quantity: ")).strip()
    print()

    #converting the serving quantity to an integer because otherwise problems were happening later in calculations
    servingQuantity = int(servingQuantity)

    # This is where we present the order back to the customer and ask them to confirm.  It will break the loop and continue if they say yes, or
    # return to the beginning of the loop to place the order again of not.  It will only accept y or n (capital or lower case)
    print("Great you picked" ,servingQuantity , "orders of " + selection +  " Is that Correct? (y or n)", end = "")
    confirmation = input().strip()
    while  confirmation.upper() != "Y" and confirmation.upper() != "N":
        confirmation = input("I'm sorry I didn't get that.  Is that Correct? (y or n)").upper().strip()
    if confirmation.upper() == "Y":
        break
    else:
        print()
        print("Sorry we made a mistake.  Let's try that again!")
        print()

# Starting the discount at 0 to create the variable
discount = 0.00

# Creating a function to calculate the sum of the prices
def subTotal():
    return (servingQuantity * price)

# Creating a function to calculate the discount according to the value of the subtotal
def firstDiscount():
    if eval('subTotal()') < 100:
         return(discount + (eval('subTotal()') * 0.05))
    elif eval('subTotal()') > 100 and eval('subTotal()') < 500:
        return(discount + (eval('subTotal()') * 0.10))
    else:
        return(discount + (eval('subTotal()') * 0.15))

# this creates a variable for the discount
discount = eval('firstDiscount()')

# This creates a variable for the total after the discount is applied
grandTotal = eval('subTotal()') - discount

print()

# This is required for the dataframe columns used to sort the information neatly
import pandas as pd

# This is creating a list for the order, called menu, so that I can insert the list into the dataframe to sort nice and neat in columns.  I had it
# all spaced out manually at first, however if values were different in length it would mess up the formatting so I figured out this which
# seems to work well!
menu = [('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _', '_ _ _ _', '_ _ _ _ _', '_ _ _ _ _'),
    (selection , formatprice , servingQuantity , "${:,.2f}".format(eval('subTotal()')))]

# This part is the dataframe in a variable called details which takes the information from menu and sorts it into columns       
details = pd.DataFrame(menu, columns =['Item','     ' 'price', '     ' 'Quantity', '       ''Subtotal'],
                        index = ['',''])      

# Here I created a function called totalto print out the order so far.  The output looks nice and neat.  Again all dollar figures are formatted accordingly.
# Then I call the function to print it out
def total():
    print(details, sep="\n")
    print("________________________________________________________________________________________________________________________")
    print("Total             ",      "${:,.2f}".format(eval('subTotal()')))
    print("Discount:  " , int(discount / eval('subTotal()') * 100) , "% =",  "${:,.2f}".format(discount))
    print("________________________________________________________________________________________________________________________")
    print("Grand Total $",      "${:,.2f}".format((eval('subTotal()') - discount)))
    print()
total()

# Here I ask if the customer is a student, only accepting y or n, upper or lower case.
student = input("Are you a student? (y or n)").strip()
while not student.upper() == "Y" and not student.upper() == "N":
    student = input("Are you a student? (y or n)").strip()
    print(student)
    
# If the customer is a student they get an additional discount.  This will be dislplayed to let them know of the discount only if it applies to them.
if student.upper() == "Y":
    customer = student
    studentTotal = grandTotal - (grandTotal * 0.10)
    print()
    print("Great! you get an additional 10 % Discount!".upper())
    print()
else:
    customer = 0

print()
print()
print()

# Here I create variables for the student total after the discount, and apply the tax separate from the variable for non-students adding tax
# This has to be distinguished so that the receipt will only display student discount information if it applies to them.
studentTotal = grandTotal - (grandTotal * 0.10)
studentFinalTotal = studentTotal * 1.13
finalTotal = grandTotal * 1.13

# This creates a list for the foundation of the student receipt.  
studentreceipt = [('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _'),
            (selection, servingQuantity, formatprice, "${:,.2f}".format(eval('subTotal()')), "${:,.2f}".format(discount), "${:,.2f}".format(grandTotal)),
            ('Student Discount of 10%', '', '', '', '', "-${:,.2f}".format((grandTotal * 0.10))),
            ('', '', '', '', 'Subtotal', "${:,.2f}".format(studentTotal)),
            ('', '', '', '', 'HST 13%', "${:,.2f}".format(studentTotal * 0.13)),
            ('', '', '', '', '', '_ _ _ _ _'),
            ('', '', '', '', 'Final Total', "${:,.2f}".format(studentFinalTotal))]

# This sorts the student receipt in columns nice and neat.
details2 = pd.DataFrame(studentreceipt, columns = ['Order','        ' 'Quantity', '     ' 'Item Price' ,'     ' 'SubTotal','     ''Discount','      ''Total'],
                        index = ['', '','','','','',''])

# This creates a list for the non-student receipt.                
regularreceipt = [('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _', '_ _ _ _ _'),
            (selection, servingQuantity, formatprice, "${:,.2f}".format(eval('subTotal()')), "${:,.2f}".format(discount), "${:,.2f}".format(grandTotal)),
            ('', '', '', '', 'HST 13%', "${:,.2f}".format(grandTotal * 0.13)),
            ('', '', '', '', '', '_ _ _ _ _'),
            ('', '', '', '', 'Final Total', "${:,.2f}".format(finalTotal))]

# This sorts the non-student receipt nice and neat.
details3 = pd.DataFrame(regularreceipt, columns = ['Order','     ' 'Quantity', '     ' 'Item Price' ,'     ' 'SubTotal','     ''Discount','      ''Total'],
                        index = ['', '','','',''])

# This creates a function to display the receipt.  It will apply the student version of the receipt if the customer is a student, and the normal receipt
# if they are not!                    
def receipt():
    print(firstName,lastName)
    print(streetNumber, streetName, "Unit #" , unitNumber) 
    print(city,",",province,",",postalCode)
    print()
    if customer == student:
        print(details2)
    elif customer == 0:
        print(details3)
    print()

# This prints the receipt to the customer!  Including the special instructions we asked for at the beginning of the program!
print("Receipt:")
print()
print("*****     Arnold's Amazing Eats II     *****")
print()
receipt()
print()
print("Special Instructions:  ", specialNotes)
    



            









