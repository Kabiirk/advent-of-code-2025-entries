from collections import deque

# Alternate Approach
# steps, ns = 30000000, [2,0,6,12,1,3]
# last, c = ns[-1], {n: i for i, n in enumerate(ns)}
# for i in range(len(ns) - 1, steps - 1):
#     c[last], last = i, i - c.get(last, i)
# print(last)

data = [2,0,6,12,1,3]

def play(n):
    for i in range(starting_number_count, n):

        last = numbers[-1]

        if len(number_indices[last]) >= 2:
            last_spoken = number_indices[last][1]
            last_last_spoken = number_indices[last][0]
            new = last_spoken - last_last_spoken
        else:
            new = 0
        numbers.append(new)

        if new not in number_indices:
            number_indices[new] = deque(maxlen=2)

        number_indices[new].append(i)

    return new

numbers = [2,0,6,12,1,3]
number_indices = {number: deque([i], maxlen=2) for i, number in enumerate(numbers)}
starting_number_count = len(number_indices)
part2 = play(30000000)

print(part2)