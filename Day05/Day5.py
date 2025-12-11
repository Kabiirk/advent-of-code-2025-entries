#open File
day5 = open("day5.txt", "r")
#initialize list to store final seat IDs
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

for line in day5:
    seat_product.append(row_col_prod(line.strip()))
day5.close()

#Returns Max Seat ID, As required by question
print(max(seat_product))