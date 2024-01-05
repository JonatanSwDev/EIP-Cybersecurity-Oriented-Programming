#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

count = 0
found = False
#Mainly intended for searches
while count < 5 and not found:
    print(f"Round number while loop {count}")
    if count == 3:
        found = True
        print('3 is found')
    count+=1
    
#Mainly intended for go over
for i in range(6):
    print(f"Round number for loop {i}")
    
world = 'Hello World!'

#Mainly intended for go over
for character in world:
    print(character)
    
