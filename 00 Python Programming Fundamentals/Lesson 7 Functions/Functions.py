#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

def greet():
    print('Hello friends')
    
def sum(num1,num2):
    return num1 + num2

greet()
print(f"2 + 5 = {sum(2,5)}") #Using numbers
print(f"Hello + World = {sum('Hello','World')}") #Using Strings
print(f"True + False = {sum(True,False)}") #Using Booleans