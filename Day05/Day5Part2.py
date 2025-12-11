#open File
day5 = open("day5.txt", "r")
seat_product = []

def row_col_prod(string):
    # After splicing string in parts depicting row and columns
    # we change B->1, F->0 and R->1, L->0
    # and convert the string->binary->integer in 1 line
    # Binary -> Integer approach is easy because everytime we encounter the alphabets,
    # our seat selection gets divided by a power of 2 successively
    # And then returns their Seat ID as per formula given in the question 
    # ( (row*8)+column = Seat ID )
    #
    # E.G. : FBFBBFFRLR --> FBFBBFF (Row) --> 0101100 --> 44 
    #                  --> RLR (Column) --> 101 --> 5
    # Seat ID = 44*8 + 5 = 357
    row = int(string[0:7].replace("B","1").replace("F","0"), 2)
    col = int(string[7:10].replace("R","1").replace("L","0"), 2)
    return (row*8)+col

#Put Seat_IDs in a list
for line in day5:
    seat_product.append(row_col_prod(line.strip()))
day5.close()

# Logic Behind this is that Only Your seat ID is missing from your list
# So we take a sum of range ALL POSSIBLE Seats then subtract sum of
# our list to find missing our missing Seat ID
#
# E.G. : your_list = [1,2,4]
#        all_possible_seat_ids = range(1 to 4) - sum(your_list)// 1-> min(your_list), 4-> max(your_list)
#        sum(all_possible seat_ids) = (1+2+3+4) = 10
#        sum(your_list) = (1+2+4) = 7
#        therefore the missing no (i.e. your Seat ID) = 10 - 7 = 3
#
# In the same analogy, the output being printed can be considered as this:
# 3 ==>   (                   1+2+3+4                    )  -    (     1+2+4    )
print({sum(range(min(seat_product), max(seat_product) +1)) - sum(seat_product)})
