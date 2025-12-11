day25 = open("day25.txt", "r")

#each line in day25.txt -> each Public Encryption Key
public_keys = []
for line in day25:
    public_keys.append(int(line))
day25.close()

#  Assigning Encryption Key
card_public_key = public_keys[0]
door_public_key = public_keys[1]

def loop_size(value_goal):
    loop = 1
    value = 1

    #Loop opertaion as mentioned in the question statement
    while True:
        value *= 7
        value = value % 20201227
        if value == value_goal:
            return loop
        loop += 1

#get the loop size for the card and door public Keys
card_loop = loop_size(card_public_key)
door_loop = loop_size(door_public_key)

# Use public key of one with loop_size of the other ([key-> door, loop->card] or [key->card , loop->door]) 
def get_common_encryption_key(public_key, loop_size):
    loop = 0
    value = 1

    # Does the same thing as loop_size() but here intead of finding the loop_size
    # we need the final value
    while(loop<loop_size):
        value *= public_key
        value = value%20201227
        loop+=1
    return value

# Printing card_loop and door_loop not required, but uncomment
# if verification is required
#print(card_loop, door_loop)

print(get_common_encryption_key(door_public_key, card_loop))
# or print(get_common_encryption_key(card_public_key, door_loop)) since both give the same answer
# Since both the answers are same , you only need one loop_size, hence
# You can do away with calculating only 1 Loop Size and using that
# to save time.

# Ref :
# 1) https://www.geeksforgeeks.org/implementation-diffie-hellman-algorithm/
# 2) https://en.wikipedia.org/wiki/Lehmer_random_number_generator


'''
     *
    /.\
   /..'\
   /'.'\
  /.''.'\
  /.'.'.\
 /'.''.'.\
 ^^^[_]^^^

  __  __                             _____  _            _       _                            _  _ 
 |  \/  |                           / ____|| |          (_)     | |                          | || |
 | \  / |  ___  _ __  _ __  _   _  | |     | |__   _ __  _  ___ | |_  _ __ ___    __ _  ___  | || |
 | |\/| | / _ \| '__|| '__|| | | | | |     | '_ \ | '__|| |/ __|| __|| '_ ` _ \  / _` |/ __| | || |
 | |  | ||  __/| |   | |   | |_| | | |____ | | | || |   | |\__ \| |_ | | | | | || (_| |\__ \ |_||_|
 |_|  |_| \___||_|   |_|    \__, |  \_____||_| |_||_|   |_||___/ \__||_| |_| |_| \__,_||___/ (_)(_)
                             __/ |                                                                 
                            |___/       
'''