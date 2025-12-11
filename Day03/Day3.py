day3 = open("day3.txt", "r")

count = 0
terrain = []

for line in day3:
    terrain.append(line.strip())
day3.close()

length = len(terrain)
tree_count = 0

i = 0
for x in terrain[::3]:
    if(x[i]=="#"):
        tree_count += 1
    i = (i+1)%len(x)


def calcTrees(h, v, inp):
  x = 0
  counter = 0
  for i in inp[::v]:
    if i[x] == "#":
      counter += 1
    x = (x+h)%len(i)
  return counter
    

print(calcTrees(3,1,terrain))