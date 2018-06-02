#!/usr/bin/env python3

##############################
#   Name: Avihu              #
# 	Sum of numbers 3 - 20    #
#   2 - 6 - 2018             #
##############################

# The numbers
array1 = [ 17, 1, 12, 54, 23, 9, 21 ]
sum_array1 = 0

# Check the numbers
for i in array1:
	if 2<i<21:       # check if the numbers between 3 to 20
		sum_array1 = sum_array1 + i 
