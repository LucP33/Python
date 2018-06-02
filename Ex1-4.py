#!/usr/bin/env python3

##############################
#   Name: Avihu              #
# 	Lamdba multiply function #
#   2 - 6 - 2018             #
##############################

# The numbers
num_list = [[ 4, 1, 7 ], [ 10, 2, 3 ], [ 1, 2, 3 ]]

sum_list= 0


for x in range (0,3):
	multi_list_func = lambda a, b, c: a * b * c     # The function
	a = int (num_list[x][0])
	b = int (num_list[x][1])
	c = int (num_list[x][2])
	multi_list  = multi_list_func(a , b, c)         # Running the function
	if multi_list > 20:
		print ( 'The result of multipling the 3 numbers "{}", "{}", "{}" is: ' .format ( a, b, c ) + str ( multi_list ))
		sum_list = sum_list + multi_list
	multi_list= 1

print ( "The sum of the results is :" + str ( sum_list ) )
