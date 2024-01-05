#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 04-01-2024
'''
print(f"Select an option:\n"
      "1. Register\n"
      "2. Log In\n"
      "3. I forgot my Password")
try:
    userData = int(input('Input a number of the option: '))
    
    match userData:
        case 1:
            print('You have been selected Register option.')
        case 2:
            print('You have been selected Log In.')
        case 3:
            print('You have been selectd I forgot my password.')
        case _:
            #Default case
            print('The option selected is not supported.')
except:
    print('The value entered is not an integer value')