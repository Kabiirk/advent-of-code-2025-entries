import sys, re
cur, pos = 1j, 0
for cmd, n in re.findall('(\w)(\d+)', open("day12.txt").read()):
    if cmd == 'F': pos += int(n)*cur
    elif cmd == 'R': cur *= 1j**(int(n)//90)
    elif cmd == 'L': cur *= 1j**(-int(n)//90)
    else: pos += {'N':1, 'S':-1, 'E':1j, 'W':-1j}[cmd] * int(n)
print(abs(pos.real) + abs(pos.imag))