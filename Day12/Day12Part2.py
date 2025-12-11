import sys, re
pos, wp = 0, 1+10j
for cmd, n in re.findall('(\w)(\d+)', open("day12.txt").read()):
    if cmd == 'F': pos += int(n)*wp
    elif cmd == 'R': wp *= 1j**(int(n)//90)
    elif cmd == 'L': wp *= 1j**(-int(n)//90)
    else: wp += {'N':1, 'S':-1, 'E':1j, 'W':-1j}[cmd] * int(n)
print(abs(pos.real) + abs(pos.imag))