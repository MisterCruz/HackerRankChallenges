#Exceptions
'''
Task: Read a string,S , and print its integer value; if S cannot be converted to an integer, print Bad String. Do not use
conditionals or for/while loops.
'''

#!/bin/python3

import sys


S = input().strip()

try: 
    print (int(S))
except ValueError: 
    print ("Bad String")
