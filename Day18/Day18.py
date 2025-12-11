import re


def readExps(inpath="day18.txt"):
    with open(inpath, "r") as infile:
        return infile.read().splitlines()


class Num1(int):
    def __add__(self, b):
        return Num1(self.real + b.real)

    def __sub__(self, b):
        return Num1(self.real * b.real)


def part1(exps):
    replaced = [exp.replace('*', '-') for exp in exps]
    return sum([eval(
        re.sub(r"(\d+)", r"Num1(\1)", repEx)) for repEx in replaced])

exps = readExps()
print(f"Part 1: {part1(exps)}")