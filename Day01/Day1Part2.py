#Input
day1 = open("day1.txt", "r")

input_list = []
for line in day1:
    input_list.append([ line[0] ,int(line[1:])])
day1.close()

'''
input_list = [
                ['R', 29], 
                ['L', 3],
                ....
             ]
'''
hits_zero = 0
marker = 50
test = []
for dir, mag in input_list:
    full, partial = divmod(mag, 100)
    hits_zero += full

    delta = -partial if dir=='L' else partial
    next_marker = marker+delta

    if marker!=0:
        if dir=='L' and next_marker<=0:
            hits_zero+=1
        if dir=='R' and next_marker>=100:
            hits_zero+=1
    
    marker = next_marker%100

print(hits_zero)