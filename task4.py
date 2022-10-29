# Name: task4.py
# Author: Michael Payne
# Date Created: October 25, 2022
# Date Last Modified: October 29, 2022
# Purpose: The purpose of this program is to convert a given speed or temperature to a different unit.  For speed it will convert to and from Miles and Kilometers, 
#          and for temperature it will convert to and from Celcius and Farenheit.    

def temperature_conversion(tempType : str, temp : int): # Function created for temperature converstion.

    if tempType == "F":

        return round((temp - 32) * 5 / 9, 2) # Calculation for converting farenheit to celcius.

    elif tempType == "C":

        return round((temp * 9 / 5) + 32, 2) # Calculation for converting celcius to farenheit.


def speed_conversion(speedType : str, speed : int): # Function created for speed conversion.

    if speedType == "1":

        return round((speed * 1.609344), 2) # Calculation to convert Miles to Kilometers.      

    elif speedType == "2":

        return round((speed * 0.62137119), 2) # Calculation to convert Kilometers to Miles.
        
        
print("This program will calculate unit conversions for speed and temperature.")

print("What would you like to convert?  Enter 1 or 2.")

print()

# This starts the loop so that if the user wants to perform another calculation after they will be returned to this point.
while True:

    unit = input(" 1) Temperature            2) Speed: ").strip() # The .strip will remove blank spaces from the beginning and end of the input.

    print()


    while unit != "1" and unit != "2": # This makes sure only valid options are accepted

        unit = input("Please enter a valid option: ").strip()

        print()


    if unit == "1":

        temp = input("Please enter a temperature to convert:").strip()

        print()


        while not temp.isnumeric(): # Making sure a number is entered for the temperature

            temp = input("Please enter a number: ").strip()

        temp = int(temp) # converting the temperature from a string to an integer.

        print("Would you like to convert from Farenheit or from Celcius? Enter F or C. ")

        tempType = input("F) Farenheit         C) Celcius: ").strip().upper() # The .upper() converts the input to a capital preventing an error for lower case

        print()


        while tempType != "F" and tempType != "C": # Only valid input is accepted and the program will not crash.

            tempType = input("Please enter a valid selection! C or F: ").strip().upper()

            print()
        

        if tempType == "F":

            conversion = temperature_conversion(tempType, temp) # Calling the temperature function for the calculation.

            output = "{} in Farenheit is equal to {} in Celcius.".format(temp, conversion) # Formatting the output.

            print(output) # Printing the answer to the user.

            print()


        elif tempType == "C":

            conversion = temperature_conversion(tempType, temp) # Calling the temperature function for the calculation.

            output = "{} in Farenheit is equal to {} in Celcius.".format(temp, conversion) # Formatting the output.

            print(output) # Printing the answer to the user.

            print()


    elif unit == "2":
        
        speed = input("Please enter a speed to convert: ").strip()

        print()


        while not speed.isnumeric(): # Ensuring only a number can be entered for the speed.

            speed = input("Please enter a number: ").strip()

        speed = int(speed) # Converts the string to an integer.

        print("Would you like to convert from MPH or from KMH? Enter 1 or 2. ")

        speedType = input( "1) MPH             2) KMH: ").strip()

        print()


        while speedType != "1" and speedType != "2": # Ensures only valid input is accepted.

            speedType = input("Please enter a valid selection! 1 or 2: ").strip()


        if speedType == "1":

            conversion = speed_conversion(speedType, speed ) # Calling the speed function to perform the calculation.

            output = "{} MPH is equal to {} KMH".format(speed, conversion) # Formatting the output.

            print(output) # Printing the output to the user.

            print()


        elif speedType == "2":

            conversion = speed_conversion(speedType, speed) # Calling the speed function to perform the calculation.

            output = "{} KMH is equal to {} MPH".format(speed, conversion) # Formatting the output.

            print(output) # Printing the output to the user.

            print()

    confirmation = input("Would you like to do another conversion? Y/N: ").upper().strip() # If another calculation is requested, the loop will return to the start.

    print()


    while  confirmation != "Y" and confirmation != "N": # Again making sure only valid input is accepted.

        confirmation = input("Would you like to do another conversion? Y/N: ").upper().strip()


    if confirmation == "N": # If no further calculations are required, the program exits.

        print()

        print("Thank you.  Have a nice day!")

        break


        
        