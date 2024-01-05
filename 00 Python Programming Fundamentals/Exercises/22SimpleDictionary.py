#!/bin/python3
import math
''' 
Created by Jonatan Gomez Garcia on 05-01-2024
'''

network = {
    "ip":"192.168.0.1",
    "domain":"Satoshi",
    "country":"secret"
}

print(network)

for key in network:
    print(f"Key: {key} - Value: {network[key]}")