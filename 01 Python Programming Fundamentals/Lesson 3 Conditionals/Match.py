#!/bin/python3
''' 
Created by Jonatan Gomez Garcua on 04-01-2024
'''

try:
    userData = int(input('Input a number: '))
    
    match userData:
        case 0:
            print('Cero')
        case 1:
            print('One')
        case 2:
            print('Two')
        case _:
            #Default case
            print('Case not supported by condition')
except:
    print('The value entered is not an integer value')