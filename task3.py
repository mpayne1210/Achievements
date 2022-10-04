# Name: WindowCalc.py
# Author: Michael Payne
# Date Created: October 03, 2022
# Date Last Modified: October 03, 2022
# Purpose: This program is a wonderful demonstration of a while loop.  It will ask for a username and only accept a name between 2 and 20 characters long.
#          It will only accept a username with at least 1 number and a capital letter.  It also removes the blank spaces before and after the username which is 
#          proven in the end output displaying the name. 

# This is the start of the loop.  All wrong inputs will return to this point.  Only a username meeting all requirements will exit the loop and see the 
# confirmation message.  Perfect!!!  The .strip will remove any blank space before and after the input.
while True:
    userName = input("Please enter your username:").strip()
    print()

    # This will prevent the user from entering a blank input.
    if bool(userName) == False:
        print("You didn't enter a username!")
    # The message displayed if the username is only one character returning to the beginning of the loop
    elif len(userName) == 1:
        print("I'm Sorry, your username must be longer than one charcter!")
        print()

    # This message will be displayed of the user enters a name more than 20 characters long, again restarting the loop.
    elif len(userName) > 20:
        print("I'm Sorry, your username cannot be moer than 20 characters in length!")
        print()

    # This makes sure that there is at least one capital in the username.
    elif userName.islower() == True:
        print("I'm Sorry, your username must contain a capital!")
        print()

    # This makes sure there is at least one number in the username.
    elif userName.isalpha() == True:
        print("I'm Sorry, your username must contain a number!")
        print()

    # This makes sure that not all numbers are entered as a username.
    elif userName.isnumeric() == True:
        print("I'm Sorry, your username cannot be all numbers!")
        print()

    # If all conditions are met the loop exits and the confirmation message is displayed.
    elif len(userName) >= 1 and len(userName) <21: 
        break

# Have a nice day in all capitals just becuase :)   
print("Thanks,", userName,"! Have a nice day!".upper())
















   
    
