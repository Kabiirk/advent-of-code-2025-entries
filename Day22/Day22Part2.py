# read the data directly into list unlike last part
decks = [[int(n) for n in i.splitlines()[1:]] for i in open('day22.txt').read().split('\n\n')]

#generate Copy of deck
copy_decks = lambda decks: [[i for i in deck] for deck in decks]

#Game Function
def game(decks):
    previous = list()
    while all(decks):
        if decks in previous:
            return decks
        else:
            previous.append(copy_decks(decks))
        
        # Popping cards for comparison
        c1, c2 = decks[0].pop(0), decks[1].pop(0)
        
        # Checking conditions as per problem
        if c1 <= len(decks[0]) and c2 <= len(decks[1]):
            subdecks = copy_decks(decks)
            subdecks[0], subdecks[1] = subdecks[0][:c1], subdecks[1][:c2]
            if game(subdecks)[0]:
                decks[0] += [c1, c2]
            else:
                decks[1] += [c2, c1]
        elif c1 > c2:
            decks[0] += [c1, c2]
        else:
            decks[1] += [c2, c1]
    return decks

decks = game(decks)
if decks[0]:
    print(sum(i * decks[0][-i] for i in range(1, 51)))
else:
    print(sum(i * decks[1][-i] for i in range(1, 51)))