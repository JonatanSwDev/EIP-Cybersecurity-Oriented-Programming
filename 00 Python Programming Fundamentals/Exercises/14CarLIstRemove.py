#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

carList = ['Mercedes','Toyota','Seat']
carList.pop(0)
carList.remove("Seat")
carList.append("KIA ")

for car in carList:
    print(f"{car} brand car")