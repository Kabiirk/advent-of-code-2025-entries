from collections import defaultdict

file = open('day10.txt', 'r')
jolts = [0]
highest = 0


for line in file:
    line = line.strip("\n")
    jolts.append(int(line))
    highest = max(highest, int(line))

jolts.append(highest + 3)

jolts = sorted(jolts)

ways = defaultdict(lambda:0)
ways[0] = 1


for i in range(1, len(jolts)):
    ways[jolts[i]] = ways[jolts[i]-1] + ways[jolts[i]-2] + ways[jolts[i]-3]


print(ways[jolts[-1]])