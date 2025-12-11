import re


def readExps(inpath="day18.txt"):
    with open(inpath, "r") as infile:
        return infile.read().splitlines()

class Num2(int):
    def __sub__(self, b):
        return Num2(self.real * b.real)

    def __mul__(self, b):
        return Num2(self.real + b.real)


def part2(exps):
    replaced = [exp.replace('*', '-').replace('+', '*')
                for exp in exps]
    return sum([eval(re.sub(r"(\d+)", r"Num2(\1)", repEx)) for repEx in replaced])

exps = readExps()
print(f"Part 2: {part2(exps)}")