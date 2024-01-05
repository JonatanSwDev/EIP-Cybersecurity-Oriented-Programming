#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

words = ['First','Second','Third']
with open("Data/WriteText.txt", "w") as f:
    for word in words:
        f.write(word + "\n")