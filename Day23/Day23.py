class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def part1(s):
    cups = list([int(x) for x in s])
    for _ in range(int(1e2)):
        rem = cups[1:4]
        goal = cups[0] - 1 if cups[0] > 1 else 9
        while goal in rem:
            goal -= 1
            if goal == 0:
                goal = 9

        idx = cups.index(goal)
        if idx == 0:
            # no change
            pass
        else:
            cups = list([cups[0]] + cups[4 : idx + 1] + rem + cups[idx + 1 :])

        cups = cups[1:] + [cups[0]]
    
    sequence = ""
    for cup in cups:
        sequence+=str(cup)

    print("Order of cups after 100 moves: ", sequence)


s = "583976241"
part1(s)