import re

day2 = open("day2.txt", "r")

new_count = 0

for line in day2:
    l = re.findall(r'(\d+)-(\d+)\s(.):\s(.*)',line) # [('15', '16', 'p', 'ppppppppppplppppp')]
    
    #shifted because index = 0 isn't considered
    index1 = int(l[0][0])-1 
    index2 = int(l[0][1])-1
    
    if( (l[0][3][index1]==l[0][2]) ^ (l[0][3][index2]==l[0][2]) ): #Validation condition
        new_count += 1 #increment counter 
day2.close()

print(new_count)
