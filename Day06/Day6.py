file = open("day6.txt","r")
productsFile = file.read()

#puts data into a list for each group i.e. ["group1, "group2", ....]
grp_answers = productsFile.split("\n\n")
ques_ans = []

for grp_answer in grp_answers:
    ques_ans.append(len(set(grp_answer.replace("\n",""))))
# What the above line does is :
#
# abced
# facdbe   ===>   "abcedfacdbecbda"   ===>   {'e', 'd', 'b', 'f', 'c', 'a'}   ===>   6
# cbda
#
# It gives the number of distinct letters in the formatted string,
# which is what's needed to be found, for each group.

#Sum of all entries in the list, which is essentially questions everyonw answered to
print(sum(ques_ans))