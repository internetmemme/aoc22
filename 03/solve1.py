#!/usr/bin/env python3
import math as m


def find_double(pair):
    for a in pair[0]:
        if a in pair[1]:
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
for bag in bags[0:-1]:
#    print(bag)
    size = len(bag)
    comps = (bag[0:m.floor(size/2)], bag[m.ceil(size/2):])
#    print(comps)
    item = find_double(comps)
    sum = sum + get_value(item)
print(sum)
