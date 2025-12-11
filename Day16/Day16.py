from collections import defaultdict; from itertools import chain, product
rules,mine,nearby = open("day16.txt").read().split('\n\n')
valid_ranges = {}
for line in rules.splitlines():
    field,valid = line.split(':')
    r1,r2 = valid[1:].split(' or ')
    s1,e1 = map(int,r1.split('-'))
    s2,e2 = map(int,r2.split('-'))
    valid_ranges[field] = [s1,e1,s2,e2]
mine = [int(x) for x in mine.split('\n')[1].split(',')]
nearby = [[int(x) for x in ticket.split(',')] for ticket in nearby.splitlines()[1:]]
valid_nearby = []
invalid,invalid_check = 0,list(valid_ranges.values())[-1]
for ticket in nearby:
    num_valid=0
    for val in ticket:
        for s1,e1,s2,e2 in valid_ranges.values():
            if s1<=val<=e1 or s2<=val<=e2:
                num_valid+=1
                break
            if [s1,e1,s2,e2] == invalid_check: invalid+=val
    if num_valid==len(ticket): valid_nearby.append(ticket)
print("Part 1:",invalid)