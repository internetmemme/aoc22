#! /usr/bin/env python3

f = open('input.txt')

text = f.read()

elves = text.split('\n\n')

maxcal = 0

for elve in elves:
    cals = elve.split('\n')
    cals = map(int, cals)
    try:
        calsum =  sum(cals)
    except:
        print('NaN')
    print(calsum)
    if calsum > maxcal:
        maxcal = calsum
#print(elves)
print(f'maxcal: {maxcal}')
