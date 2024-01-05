#!/bin/python3
import math
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

def sumF(num1,num2):
    return num1 + num2

def unlimitedSum(*args):
    return sum(list(args))

print(f"2 + 3 = {sumF(2,3)}")
print(f"2 + 3 + 4 + 5 = {unlimitedSum(2,3,4,5)}")