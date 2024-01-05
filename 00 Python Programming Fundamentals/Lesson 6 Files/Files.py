#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

#Read all text
file = open("Text to read.txt", "r")
print(file.read())
file.close()

#Read all text using with (is not necessary to colse file)
with open("Text to read.txt", "r") as f:
    print(f.read())
    print(f.closed)
print(f.closed)

#Read line
file = open("Text to read.txt", "r")
print(file.readline())
file.close()

#Read each line
file = open("Text to read.txt", "r")
for line in file.readlines():
    print(line.replace("\n",""))
file.close()

#Write in file
file = open("Text to write.txt", "w")
file.write("Writting using python.")
file.close()

#Append to file
file = open("Text to write.txt", "a")
file.write("\nGood Morning.")
file.close()
