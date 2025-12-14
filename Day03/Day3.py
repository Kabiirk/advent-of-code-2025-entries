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
    selected_pow = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            selected_pow = max(selected_pow, (bank[i]*10) + bank[j] )

    total_output_joltage += selected_pow
    
print(total_output_joltage)
