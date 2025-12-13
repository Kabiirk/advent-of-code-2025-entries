import re

# Data Parsing & Setup
id_ranges = None
with open('Day2.txt', 'r') as f:
    for line in f:
        id_ranges = line.split(',')
f.close()

for r in range(len(id_ranges)):
    l = re.findall(r'(\d+)-(\d+)', id_ranges[r])
    id_ranges[r] = [int(l[0][0]), int(l[0][1])]
id_ranges.sort(key=lambda x: x[0])

# Actual Solution
invalid_sum = 0
for low, high in id_ranges:
    for i in range(low, high+1):
        s = str(i)
        mid = len(s)//2
        s_half = s[:mid]
        if s_half+s_half == s:
            # Invalid
            # print(i)
            invalid_sum += i

print(invalid_sum)
