day3 = open("day3.txt", "r")

#Put file data into list
terrain = []
for line in day3:
    terrain.append(line.strip())
day3.close()

#Function to calculate Trees Encountered
def calcTrees(h, v, inp):
  x = 0
  counter = 0
  for i in inp[::v]:
    if i[x] == "#":
      counter += 1
    x = (x+h)%len(i)
  return counter
    

a = calcTrees(1,1,terrain)
b = calcTrees(3,1,terrain)
c = calcTrees(5,1,terrain)
d = calcTrees(7,1,terrain)
e = calcTrees(1,2,terrain)

print(a*b*c*d*e)