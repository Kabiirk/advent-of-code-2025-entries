file = open("day6.txt","r")
productsFile = file.read()

#puts data into a list for each group i.e. ["group1, "group2", ....]
grp_answers = productsFile.split("\n\n")

def intersection_of_multiple_strings(l):
    setlist = [ set(i) for i in l ]
    common_ans = len(set.intersection(*setlist))
    return(common_ans)
# What the above Function does :
#
#                                      [{'e', 'd', 'c', 'a', 'b'}, 
# ["abced", "facdbe", "cbda"]   ===>   {'e', 'd', 'c', 'f', 'a', 'b'},   ===>   {set1 ∩ set2 ∩ set3 ∩......}   ===>   6
#                                      {'c', 'a', 'd', 'b'}]                    (basically a set having the          (length of the final set)
#                                                                               intersection of all sets in
#                                                                               the list)

for i in range(len(grp_answers)):
    grp_answers[i] = grp_answers[i].split("\n")
# What the above line does is :
#
# abced
# facdbe   ===>   ["abced", "facdbe", "cbda"]
# cbda

#Applies the function
for j in range(len(grp_answers)):
    grp_answers[j] = intersection_of_multiple_strings(grp_answers[j])

#Sum of all entries in the list, which is essentially questions everyonw answered to
print(sum(grp_answers))