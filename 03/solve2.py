#!/usr/bin/env python3
import math as m


def find_double(tri):
    for a in tri[0]:
        if a in tri[1] and a in tri[2]:
            return a
    return "error"

def get_value(item):
    value = 0
    if item.isupper():
        value = ord(item) - 38
    else:
        value = ord(item) - 96
    print(f"{item} : {value}")
    return value

sum = 0 
    
f = open('input')
bags = f.read()
bags = bags.split('\n')

i = 0

while i < len(bags)-1:
    trip = (bags[i], bags[i+1], bags[i+2])
    item = find_double(trip)
    sum = sum + get_value(item)
    i = i + 3
print(sum)
