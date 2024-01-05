#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''
#Simple initalization
numbers = [0,1,2,3]
listData = [3,"Jonatan",True,3.15]

#Simple print
print(numbers[0],numbers[3])
print(listData[0],listData[1],listData[3])
print(f"Lenght of numbers: {len(numbers)}\nLenght of listData: {len(listData)}")

#Simple loop
for data in listData:
    print(data)

#Append
listData.append('One mode data')
print(f"Lenght of numbers: {len(numbers)}\nLenght of listData: {len(listData)}")

#Insert
listData.insert(2,'Data inserted in position two')
print(listData)

#Reverse
numbers.reverse()
print(numbers)

#Clear
numbers.clear()
print(numbers)

#Contain
print(listData.__contains__("Jonatan"))

#Contain condition
if "Jonatan" in listData:
    print("Helo Jonatan")

#Remove
listData.remove(True)
print(listData)

#Pop remove
listData.pop(0)
print(listData)

#Only print a range in the list
print(listData[2:4])

