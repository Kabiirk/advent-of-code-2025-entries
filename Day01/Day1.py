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

for dir, mag in input_list:
    if dir == 'R':
        marker += mag
    if dir == 'L':
        diff = marker - mag
        marker = 100 + diff if diff<0 else diff
    
    marker = marker%100
    if marker==0:
        hits_zero+=1

print(hits_zero)
