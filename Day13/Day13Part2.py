def parse(f):
    departure = int(f.readline())
    tokens = f.readline().split(",")
    busses = [(busIdx, int(bus)) for busIdx, bus in enumerate(tokens) if bus != 'x']
    f.close()
    return departure, busses


def partTwo(departure, busses):
    _, period = busses[0]
    t = 0
    for busIdx, bus in busses[1:]:
        offset = None
        while True:
            if (t + busIdx) % bus == 0:
                if offset is None:
                    offset = t
                else:
                    period = t - offset
                    break

            t += period

    return offset



departure, busses = parse(open("day13.txt"))

print(partTwo(departure, busses))

# Also reffer to :
# Chineese Remainder theorem