'''
Coordinate system:
       / \     / \
     /     \ /     \
    |  0,-1 |  1,0  |
    |  nw   |  ne   |
   / \     / \     / \
 /     \ /     \ /     \
| -1,-1 |  0,0  |  1,1  |
|   w   |  ref  |   e   |
 \     / \     / \     /
   \ /     \ /     \ /
    | -1,0  |  0,1  |
    |  sw   |  se   |
     \     / \     /
       \ /     \ /
'''

def part1(tiles_list, direction):
    blacks = set()
    for line in tiles_list:
        i = 0
        steps = []
        while i < len(line):
            if line[i] == 's' or line[i] == 'n':
                steps.append(line[i: i+2])
                i = i + 2
            else:
                steps.append(line[i])
                i = i + 1

        x = 0
        y = 0
        for step in steps:
            x = x + direction[step][0]
            y = y + direction[step][1]
        if (x, y) not in blacks:
            blacks.add((x, y))
        else:
            blacks.remove((x, y))

    return len(blacks)#, blacks


with open('day24.txt', 'r') as f:
    f = f.readlines()
    tiles_list = [line.strip() for line in f]

direction = {'nw':(-1, -1), 'sw':(1, -1), 'ne':(-1, 1),
             'se':(1, 1), 'w':(0, -2), 'e':(0, 2)}

ans = part1(tiles_list, direction)
print(ans)