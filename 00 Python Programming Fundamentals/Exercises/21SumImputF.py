#!/bin/python3
import math
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

def unlimitedSum(numbers):
    return sum(numbers)

numberList = []

try:
    option = "y"
    while option.lower() == 'y' or option == "":
        numberList.append(int(input('Input a integer number: ')))
        option = input('Do you want to continue? Y/n: ')
    
    print(f"The sum of numbers {numberList} is {unlimitedSum(numberList)}")
except:
    print('The value entered is not compatible with the execution.')
