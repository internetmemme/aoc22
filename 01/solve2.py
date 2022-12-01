#! /usr/bin/env python3

f = open('input.txt')

text = f.read()

elves = text.split('\n\n')

elvecals = []

for elve in elves:
    cals = elve.split('\n')
    cals = map(int, cals)
    try:
        calsum =  sum(cals)
    except:
        print('NaN')
    print(calsum)
    elvecals.append(calsum)
#print(elves)
elvecals.sort()
top3 = elvecals[-1] + elvecals[-2] + elvecals[-3]
print(top3)                    
