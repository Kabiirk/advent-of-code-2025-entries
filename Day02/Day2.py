import re

day2 = open("day2.txt", "r")

count = 0

for line in day2:
    l = re.findall(r'(\d+)-(\d+)\s(.):\s(.*)',line) # [('15', '16', 'p', 'ppppppppppplppppp')]
    instance_of_letter = l[0][3].count(l[0][2]) # no. of 'p' in 'ppppppppppplppppp'
    if( instance_of_letter >= int(l[0][0]) and instance_of_letter <= int(l[0][1]) ): #Validation condition
        count += 1 #increment counter 
day2.close()

print(count)
