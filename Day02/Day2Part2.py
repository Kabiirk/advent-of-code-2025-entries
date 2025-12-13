import re
import math

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
def is_invalid(num_s):
    if len(num_s)<=1:
        return False
    
    n = len(num_s)

    for l in range(1, int(math.sqrt(n))+1):
        if n%l==0:
            divisors = set([l, n//l])
            for seq_len in divisors:
                if seq_len==n:
                    continue
                
                sequence = num_s[:seq_len]
                repetitions = n//seq_len

                if num_s == sequence*repetitions:
                    # Uncomment to debug
                    # print(f"ID is invalid: pattern '{sequence}' repeats {repetitions} times.")
                    return True
    return False

invalid_sum = 0
for low, high in id_ranges:
    for i in range(low, high+1):
        s = str(i)
        if is_invalid(s):
            invalid_sum+=i

print(invalid_sum)
