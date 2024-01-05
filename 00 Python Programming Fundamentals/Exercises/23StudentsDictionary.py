#!/bin/python3
import math
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''
students = [{"name":"Jonatan","surname":"Gomez Garcia","DNI":"00000000A"},
            {"name":"Pepito","surname":"Perez Atocha","DNI":"00000000B"},
            {"name":"Jaimito","surname":"Elde Loschistes","DNI":"00000000C"}]


for student in students:
    print(student)

for student in students:
    for key in student:
        #This ternary expresion is to capitalize only if is not capitalized. The DNI are Initials
        print(f"{key.capitalize() if key[0].islower() else key}: {student[key]}") 
    
    