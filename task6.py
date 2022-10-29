# Name: task6.py
# Author: Michael Payne
# Date Created: October 25, 2022
# Date Last Modified: October 29, 2022
# Purpose: The purpose of this program is to have the user enter a string of numbers separated by a comma. The program will take each number, decide if it 
#          is a prime number of not, and place it in a new list on that determination.  It will then print out a list of the prime and non-prime numbers 
#          entered by the user.  

def primeCheck(): # This creates a function to calculate if the numbers entered are prime or not, and act accordingly.

    for num in numList: # This starts a loop that will go through the list of numbers entered by the user.


        if num > 1:


            for i in range(2,num): # This is another loop and this time it is checking the number entered by the user against the algorithm deciding if it is prime.


                if (num % i) == 0: # The calculation for determining if a number is a prime number.

                    nonPrime_list.append(num) # If the number is determined not to be prime, it is added to the nonprime list.

                    break

            else:

                prime_list.append(num) # If the number is prime, it is added to the prime list.


        else:

            nonPrime_list.append(num) # 1 or any negative number are not prime numbers.


separator = ',' # This tells the program where to separate the list when printing the output.

prime_list = [] # Creates the empty prime list.

nonPrime_list = [] # Creates the empty non-prime list.

num = input("Please enter a list if numbers separated by commas: ")

numList = num.split(",") # Taking the input from the user using the comma as a separator, and creating a list.

numList = list(map(int, numList)) # This converst the numbers in the list from a string into integers.  Was getting errors other ways and found this worked.

primeCheck() # Calling the primecheck function to sort through the list entered and make its calculations.

print("The prime numbers are", separator.join(map(str, prime_list))) # printing the list of prime numbers adding the separator.

print("The non-prime numbers are", separator.join(map(str,nonPrime_list))) # printing the list of non-prime numbers adding the separator.

    





