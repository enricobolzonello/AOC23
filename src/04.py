from utils.api import get_input
import re

input_str = get_input(4)

def part1():
    total_sum = 0
    pattern = re.compile('[\d]+')
    for line in input_str.splitlines():
        a = pattern.findall(line)
        winning = a[1:11]
        own = a[11:]
        wins = len(set(winning).intersection(own))

        if wins == 0:
            total_sum += 0
        elif wins == 1:
            total_sum += 1
        else:
            total_sum += 2**(wins-1)
    print("part 1: ", total_sum)

def part2():
    pattern = re.compile('[\d]+')
    lines = input_str.splitlines()
    n_original = len(lines)
    copy_cards = [1] * n_original
    for i,line in enumerate(lines):
        a = pattern.findall(line)
        winning = a[1:11]
        own = a[11:]
        wins = len(set(winning).intersection(own))

        for j in range(wins):
            copy_cards[i + j + 1] += copy_cards[i]
        
    print("part 2: ",sum(copy_cards))
        

part1()
part2()