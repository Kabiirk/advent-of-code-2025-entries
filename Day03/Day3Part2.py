# Data Parsing & Setup
power_banks = []
with open('day3.txt', 'r') as f:
    for line in f:
        line = line.strip()
        power_banks.append(list( map(lambda x: int(x), line) ))
f.close()

# Actual Solution
total_output_joltage = 0

for bank in power_banks:
    max_pow = []
    for digit in bank:
        stack = []
        can_drop = len(bank) - 12
        
        for digit in bank:
            while stack and can_drop>0 and stack[-1]<digit:
                stack.pop()
                can_drop-=1
            stack.append(digit)
        max_pow=stack

    total_output_joltage += int( "".join( map(str, max_pow[:12]) ) )

print(total_output_joltage)