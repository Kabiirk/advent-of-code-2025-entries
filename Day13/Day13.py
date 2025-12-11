day13 = open("day13.txt", "r")

#Put data in a list
input_list = []
for line in day13:
    input_list.append(line.strip())
day13.close()

# Separating data for easier usage, can be omitted to save space
# but list indexing would need to be used , which makes code
# tougher to read 
departure_timestamp = int(input_list[0])
bus_ids = input_list[1].replace("x","").replace(","," ").split()
bus_ids = list(map(int, bus_ids)) 

# compute the closest multiple greater than timestamp
def difference_of_colsest_multiple_greater(departure, time_step):
    original_timestamp = departure

    if time_step>departure:
        return time_step
    z = int(time_step/2)
    departure = departure + time_step
    departure = departure - (departure%time_step)

    return departure-original_timestamp

time_difference = [] # Store time diff in a list
difference_dict = {} # Store bus_ids with their time diff as key,value pairs

for bus_id in bus_ids:
    #uses extra variable, but reduces extra function call
    d = difference_of_colsest_multiple_greater(departure_timestamp, bus_id)

    time_difference.append(d)
    difference_dict[bus_id] = d

# Find the bus_id corresponding to the minnimun time diffrence
# Then print their product 
for key, value in difference_dict.items():
    if value==min(time_difference):
        print(key*value)