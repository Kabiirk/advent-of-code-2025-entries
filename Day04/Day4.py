# Data Parsing & Setup
paper_roll_rows = []
with open('day4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        paper_roll_rows.append(line)
f.close()

# Actual Solution
paper_rolls_can_move = 0
HEIGHT = len(paper_roll_rows)
WIDTH = len(paper_roll_rows[0])
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

for h in range(HEIGHT):
    for w in range(WIDTH):
        if paper_roll_rows[h][w]=='@':
            surround_score = 0 # How many paper rolls surround each role
            for d_h, d_w in dirs:
                if 0 <= h + d_h < HEIGHT and 0 <= w + d_w < WIDTH:
                    if paper_roll_rows[ h+d_h ][ w+d_w ]=='@':
                        surround_score += 1
            if surround_score<4:
                paper_rolls_can_move+=1

print(paper_rolls_can_move)