#!/usr/bin/env python3

####################
#   Name: Avihu    #  
# 	Arry Check     #
#   2 - 6 - 2018   #
####################

# define the function
def array_func ( array1, num ):
    length_array = len (array1)
    print (" The sum of the array: " + str ( sum ( array1 )) )
    print (" The length of the array: " + str ( length_array ) )
    print (" The Check number is: " + str ( num ) )
    if length_array < num:
        return (0)
    else:
        return (1)

# array & numer input        
array_list = [ 2, 5, 8, 9, 17, -1, 26, -19 ]
num_test  = 9

# check the array & return status
if ( array_func ( array_list, num_test ) ) == 0:
	print ( "True" )  # Print if array_func return 0
else:
	print ( " False " )  # Print if array_func return 1
     
