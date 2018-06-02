#!/usr/bin/env python3

##############################
#   Name: Avihu              #
# 	Sum - Multiply - Devide  #
#   2 - 6 - 2018             #
##############################

# Get numbers from User
num1 = int ( input ( 'Enter first number: ' ) )
num2 = int ( input ( 'Enter second number: ' ) )

# Print SUM
print ( 'The sum of the numbers: ' + str ( num1 + num2 ))
# Print Multiply
print ( 'The multiply of the numbers: ' + str ( num1 * num2 ))
# Print Devide
print ( 'The divide of the numbers: :' + str ( num1 / num2 ))

#Check for the bigger number
if num1 == num2:
	print ( 'The numbers are equal' )
else:
	if num1 > num2:
		print ( 'The biger number is ' + str ( num1 ) )
	else:
		print ( 'The biger number is ' + str ( num2 ) )

