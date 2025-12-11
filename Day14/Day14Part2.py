def read(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f:
            a, b = line.split(' = ')
            if a == "mask":
                data.append(b.strip())
            else:
                address = int(a[4:-1])
                value = int(b)
                data.append((address, value))

    return data

def flip(n, cache={}):
    # A gray code for looping through integers while changing only one bit per
    # iteration
    if n not in cache:
        if n == 1:
            cache[n] = [0]
        else:
            cache[n] = flip(n-1) + [n-1] + flip(n-1)

    return cache[n]

def part1(s, mem, address, value):
    x1 = int(s.replace('X', '1'), 2)
    x0 = int(s.replace('X', '0'), 2)

    mem[address] = (value & x1) | x0

def part2(s, mem, address, value):
    x0 = int(s.replace('X', '0'), 2)
    address |= x0

    f = [1 << (len(s)-1-i) for i, x in enumerate(s) if x == "X"]

    mem[address] = value
    for flip_bit in flip(len(f)):
        address ^= f[flip_bit]
        mem[address] = value

def solve(data, f=part1):
    mem = {}
    for line in data:
        if type(line) is str:
            mask = line
        else:
            f(mask, mem, *line)
    return mem

data = read("day14.txt")
mem = solve(data)
mem = solve(data, f=part2)
print(sum(mem.values()))