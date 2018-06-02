#!/usr/bin/env python3

####################
#   Name: Avihu    #  
# 	Add Function   #
#   2 - 6 - 2018   #
####################

# define the functions
# ADD function
def add ( num1, num2 ):
    res = num1 + num2
    return ( res )

# Multiply function with ADD function
def mul ( num1, num2 ):
	num3 = 0
	for i in range (num2):
		num3 = add ( num3 , num1 )
	return ( num3 )

# Getting to numbers
numA = int ( input ( "Enter a nmber: " ))
numB = int ( input ( "Enter a nmber: " ))

# Print the sum & multiply results
print ( "The sum of the numbers is: " + str ( add ( numA, numB ) ) )
print ( "The multiply of the numbers is: " + str ( mul ( numA, numB ) ) )
