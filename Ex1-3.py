#!/usr/bin/env python3

##############################
#   Name: Avihu              #
# 	Longer string Function   #
#   2 - 6 - 2018             #
##############################

# define the function
def longer_str ( str1, str2 ):
    if len(str1) < len(str2):
        return ( str2 )
    else:
        return ( str1 )

# The strings        
string1 = 'Hi'
string2 = 'Hello'
string3 = 'Shalom'
string4 = 'Bye Bye'

#Printout of the function
print ( 'The longer word between "{}" and "{}" is:' .format(string1 , string2 ) + longer_str ( string1, string2 )  )
print ( 'The longer word between "{}" and "{}" is:' .format(string3 , string4 ) + longer_str ( string3, string4 )  )
