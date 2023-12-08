from utils.api import get_input
import re
import math

input_str = get_input(8)

lines = input_str.splitlines()

directions = lines[0]

network = {}
for line in lines[2:]:
    pattern = re.compile('[A-Z]+')
    a = pattern.findall(line)
    network[a[0]] = (a[1],a[2])

def solve(start, end):
    found = False
    i = 0
    n = len(directions)
    while not found:
        temp = 0 if directions[i%n] == "L" else 1

        start = network[start][temp]

        i+=1

        if start.endswith(end):
            found = True
    return i

def part1():
    root = "AAA"
    print("part 1: ", solve(root, "ZZZ"))

def part2():
    ret = 1
    for n in network:
        if n.endswith('A'):
            ret = math.lcm(ret, solve(n, "Z"))
    print("part 2: ", ret)

part1()
part2()