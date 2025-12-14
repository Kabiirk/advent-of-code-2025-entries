# Data Parsing & Setup
paper_roll_rows = []
with open('test.txt', 'r') as f:
    for line in f:
        line = line.strip()
        paper_roll_rows.append(list(line))
f.close()

# Helper Functions
def print_floor( roll_rows ):
    for r in roll_rows:
        print(''.join(r))

def can_move(h, w):
    surround_score = 0 # How many paper rolls surround each role
    for d_h, d_w in dirs:
        if 0 <= h + d_h < HEIGHT and 0 <= w + d_w < WIDTH:
            if paper_roll_rows[ h+d_h ][ w+d_w ]=='@':
                surround_score += 1
    if surround_score<4:
        return [h, w]
    return [-1,-1]

# Actual Solution
paper_rolls_can_move = 0
HEIGHT = len(paper_roll_rows)
WIDTH = len(paper_roll_rows[0])
queue = []
removed = set()
dirs = [
            [-1, -1], # Top Left
            [-1, 0], # Top
            [-1, 1], # Top Right
            [0, -1], # Left
            [0, 1], # Right
            [+1, -1], # Bottom Left
            [+1, 0], # Bottom
            [+1, +1], # Bottom right
       ]

# 1st Pass
for h in range(HEIGHT):
    for w in range(WIDTH):
        if paper_roll_rows[h][w]=='@':
            res = can_move(h, w)
            if res[0]!=-1:
                queue.append([h,w])
                removed.add((h,w))
                paper_rolls_can_move+=1
for x,y in queue:
    paper_roll_rows[x][y] = 'x'

# Uncomment to see 1st pass of Simultation
# print_floor(paper_roll_rows)
# print('===============')

# Subsequent passes (Multi-source BFS)
while queue:
    # Pop all roll coordinates from same 'level'/pass of removed rolls
    temp_queue = [] # Temp queue to hold neighbors of all rolls removed at the same pass, we check these co-ords in next pass
    t = 0
    for i in range(len(queue)):
        # Traverse all removed rolls at thegiven pass
        h = queue[i][0]
        w = queue[i][1]
        nei = []
        for dh, dw in dirs:
            # Generate valid neighbors (in floor bounds, and has a roll which hasn't been removed)
            if 0 <= h+dh < HEIGHT and 0 <= w+dw < WIDTH and paper_roll_rows[h+dh][w+dw]=='@':
                nei.append([h+dh, w+dw])

        for nh, nw in nei:
            # Check if neighbor valid to remove
            res = can_move(nh, nw)
            if res[0]!=-1 and (nh, nw) not in removed:
                removed.add((nh, nw)) # Populate next level of rolls (neighbor of active rolls)
                temp_queue.append([nh, nw])
                paper_rolls_can_move+=1
                t+=1
    queue = temp_queue # Assign next level of rolls as current(moving onto all neighbors of rolls removed in the previous pass)
    for x,y in queue:
        paper_roll_rows[x][y] = 'x'

    # Uncomment to see subsequent pass of Simultation
    # print_floor(paper_roll_rows)
    # print(f'removed {t} rolls.')
    # print('===============')

print(paper_rolls_can_move)
