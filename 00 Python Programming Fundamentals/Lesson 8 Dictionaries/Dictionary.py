#!/bin/python3
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

#If 2 values are asigned at the same key, the last value will be overwritten.
dictionary = {
    "ip":"127.0.0.1",
    "domain":"localhost",
    "geo":"local"
}

print(dictionary["ip"])

#Browse the dictionary content
for key in dictionary: #Same of for key in dictionary.keys()
    print(key) #To print the keys.
    print(dictionary[key]) #To print the values asociated with the keys.
    
#Append data to dictionary
dictionary["location"] = "Spain"
print(dictionary)

#Remove item from dictionary
dictionary.pop("ip")
del dictionary["location"]
print(dictionary)

#Clear dictionary
dictionary.clear()
print(dictionary)