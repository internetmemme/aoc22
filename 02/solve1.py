#!/usr/bin/env python3

def get_value_pick(pick):
    if pick == 'X':
        return 1
    if pick == 'Y':
        return 2
    if pick == 'Z':
        return 3
    print(f"error in get_value_pick: {pick}")
    return -1

def get_value_outcome(pair):
    opp = pair[0]
    us = pair[1]
    if opp == 'A':
        #rock
        if us == 'X':
            #rock
            return 3
        if us == 'Y':
            #paper
            return 6
        if us == 'Z':
            return 0
    if opp == 'B':
        #paper
        if us == 'X':
            #rock
            return 0;
        if us == 'Y':
            #paper
            return 3
        if us == 'Z':
            #scissors
            return 6
    if opp == 'C':
         #scissors
        if us == 'X':
            #rock
            return 6;
        if us == 'Y':
            #paper
            return 0
        if us == 'Z':
            #scissors
            return 3

def get_value(pair):
    value = 0;
    value = value + get_value_pick(pair[1])
    value = value + get_value_outcome(pair)
    return value

f = open('input')
score = 0
for pair in f:
    # pair.strip('\n')
    # pair = pair.split(' ')
    # print(pair)
    pair = (pair[0], pair [2])
   # print(pair)
    score = score + get_value(pair)

print(score)
