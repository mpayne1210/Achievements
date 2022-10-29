# Name: task5.py
# Author: Michael Payne
# Date Created: October 25, 2022
# Date Last Modified: October 29, 2022
# Purpose: The purpose of this program is to generate and print a dictionary containg the numbers 1 through 10 along with the cubic values of each. 
 
dicts = {} # Creating an emtpy dictionary to begin.

for i in range(1,11):  # This creates a loop that will cycle through the numbers 1 to 10.

    dicts[i] = i ** 3 # This adds the cubic value of each number to the dictionary created at the beginning of the program.

print(dicts) # This prints the new dictionary with the cubic values in it.


