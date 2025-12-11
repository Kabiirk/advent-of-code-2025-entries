with open("day22.txt") as f:
    player_info = f.read()

#Initial List with all data
data = player_info.split("\n\n")

# Separate list of Player 1's cards and convert string => integer
player1 = data[0].split("\n")[1:][::-1]
player1 = list(map(int, player1))

# Separate list of Player 2's cards and convert string => integer
player2 = data[1].split("\n")[1:][::-1]
player2 = list(map(int, player2))

while( (player1 and player2) ):
    # Pop Cards at the top of each player's stack to be compared
    card_p1 = player1.pop()
    card_p2 = player2.pop()

    # based on comparison, put in appropriate stack at the bottom
    if(card_p1 > card_p2):
        player1.insert(0, card_p1) 
        player1.insert(0, card_p2)
    else:
        player2.insert(0, card_p2) 
        player2.insert(0, card_p1) 

#Calculating the Result
result = 0
for i in range(1,len(player1)+1):
    result += player1[i-1]*i
print(result)