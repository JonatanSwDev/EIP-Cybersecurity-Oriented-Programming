#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

with open("Data/WriteText.txt", "r") as f:
    for word in f:
        print(f"This is the {word[:-1]} line")