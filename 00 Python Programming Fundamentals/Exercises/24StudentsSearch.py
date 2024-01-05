#!/bin/python3
import math
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''
students = [{"name":"Jonatan","surname":"Gomez Garcia","DNI":"00000000A"},
            {"name":"Pepito","surname":"Perez Atocha","DNI":"00000000B"},
            {"name":"Jaimito","surname":"Elde Loschistes","DNI":"00000000C"}]

count = 0
found = False

while count < len(students) and not found:
    if students[count]["DNI"] == "00000000B":
        found = True
        print(f"Student 00000000B found.\nFull name: {students[count]['name']} {students[count]['surname']}")
    count += 1
    
if not found:
    print('Student doen\'t found')
    
    