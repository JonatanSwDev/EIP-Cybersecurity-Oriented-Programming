#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''
try:
    number = int(input('Type a number between 0 and 10: '))
    i = 0
    found = False
    while i < 11 and not found:
        if i == number:
            found = True
            print(f"Number {number} found. Ending loop")
        i += 1

    if not found:
        print('The value typed is not a integer value between 0 and 10')
        
except:
    print('The value typed is not compatible with the execution')