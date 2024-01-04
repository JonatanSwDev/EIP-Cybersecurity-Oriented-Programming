#!/bin/python3
''' 
Created by Jonatan Gomez Garcua on 04-01-2024
'''

try:
    userData = int(input('Input the number 2: '))
    
    if userData == 2:
        #First condition is true
        print('Thanks for input the number 2')
    elif userData < 0:
        #Second condition is true
        print('You have been inputted a negative number')
    else:
        #If both conditions are false
        print('Case not supported by condition')
except:
    print('The value entered is not an integer value')