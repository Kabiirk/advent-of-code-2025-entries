from collections import defaultdict, deque

# Reading input
filename = "Day7.txt"
rules = {}

# E.g.:
# Line = "pale cyan bags contain 2 posh black bags, 4 wavy gold bags, 2 vibrant brown bags."
#
# s = line.split(' bags contain ') = ['pale cyan', '2 posh black bags, 4 wavy gold bags, 2 vibrant brown bags.']
# now s[0] -> main bag which holds other bags as per statement
# and s[1] -> has all the bags s[0] can/cannot hold and their quantity
#
# s[1] = '2 posh black bags, 4 wavy gold bags, 2 vibrant brown bags.'
#
# s[1].split(', ') = ['2 posh black bags', '4 wavy gold bags', '2 vibrant brown bags.']
# (3 values in list therefore our for iterator runs 3 times)
#
# We then iterate through list from s[1].split(", ") to get bag colors
# and their quantity which s[0] holds (all vaues of comp through the loop): 
#
# iteration 1
# comp:  2 posh black bags
# words:  ['2', 'posh', 'black', 'bags']
#
# iteration 2
# comp:  4 wavy gold bags
# words:  ['4', 'wavy', 'gold', 'bags']
#
# iteration 3
# comp:  2 vibrant brown bags.
# words:  ['2', 'vibrant', 'brown', 'bags.']
#
# for each of these comp-word pairs, we append it into a dictionary in form 'color: frequency'
# (words[1] + ' ' + words[2] is just to get the full fancy color name (eg. posh black) as key)
#
# as our end dictionary we get :
# {'pale cyan': defaultdict(<class 'int'>, {'posh black': 2, 'wavy gold': 4, 'vibrant brown': 2})}
# {our parent bag color : {color1: no. parent can hold , color2: no. parent can hold, .... }
# which is our statement as a dictionary
 
with open(filename,'r') as file_:
    for line in file_:
        s = line.strip().split(' bags contain ')
        
        content = defaultdict(int)
        for comp in s[1].split(', '):
            words = comp.split(' ')
            if words[0] != 'no':
                content[words[1] + ' ' + words[2]] = int(words[0])
        rules[s[0]] = content


bags = set(['shiny gold'])
l = 0

# Continue to execute this function until no new items are added to the set bags
while len(bags) > l:
    l = len(bags)
    # Iterate over the rules, if the rule contains anything in the set bags, add the key for that rule to the set bags
    #i.e. if any value for the parent bag key == 'shiny gold', add that color to the list
    [bags.add(key) for key in rules if any(color in rules[key].keys() for color in bags)]

# using set because we need the number of distinct colors that can hold the shiny gold bag
# -1 because one of the elements in that list was shiny gold
# i.e. the color that whose number we are supposed to find
print(f'Answer part 1: {len(bags)-1}')