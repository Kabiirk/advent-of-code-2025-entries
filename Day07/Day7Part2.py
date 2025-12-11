from collections import defaultdict, deque

# Reading input
filename = "Day7.txt"
rules = {}

with open(filename,'r') as file_:
    for line in file_:
        s = line.strip().split(' bags contain ')
        
        content = defaultdict(int)
        for comp in s[1].split(', '):
            words = comp.split(' ')
            if words[0] != 'no':
                content[words[1] + ' ' + words[2]] = int(words[0])
        rules[s[0]] = content


bags2 = defaultdict(int)
q = deque([('shiny gold',1)])

while len(q) > 0:
    color,amount = q.pop()

    for key in rules[color]:
        q.append((key, rules[color][key] * amount))
        bags2[key] += rules[color][key] * amount
                     
print(f'Answer part 2: {sum(bags2.values())}')