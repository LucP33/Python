#!/usr/bin/env python3

#################################################
#   Name: Avihu                                 #
# 	Sum higher then 30 or number bigger then 10 #
#   2 - 6 - 2018                                #
#################################################
i=0
num_sum = 0
while i < 11:
    num_sum = num_sum + i
    if num_sum > 30:
	    break
    i = int ( input ( 'Enter a number: ') )    
print ( 'The sum of the numbers is:' + str ( num_sum ) )
