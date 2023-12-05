from utils.api import get_input
import re

input_str = get_input(5)

def part1():
    parts = input_str.split('\n\n')
    seeds = [int(x) for x in parts[0].split(':')[1].split()]
    parts.pop(0)

    maps = [[] for _ in parts]
    for i,part in enumerate(parts):
        for line in part.splitlines()[1:]:
            numbers = [int(x) for x in line.split()]
            maps[i].append((numbers[1], numbers[1] + numbers[2], numbers[0] - numbers[1]))

    mins = []
    for seed in seeds:
        # make all maps
        for tuples in maps:
            for (range_start, range_end, difference) in tuples:
                if range_start <= seed <= range_end:
                    seed += difference
                    break
        mins.append(seed)
    print("part 1: ", min(mins))

def part2():
    parts = input_str.split('\n\n')
    seeds = [int(x) for x in parts[0].split(':')[1].split()]
    seeds_pairs = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0,len(seeds),2)]
    parts.pop(0)
    
    maps = [[] for _ in parts]
    for i,part in enumerate(parts):
        for line in part.splitlines()[1:]:
            numbers = [int(x) for x in line.split()]
            maps[i].append((numbers[1], numbers[1] + numbers[2], numbers[0]))

    for pair in seeds_pairs:
        remain = [pair]
        result = []

        for tuples in maps:
            while remain:
                curr = remain.pop() 
                for (range_start, range_end, destination) in tuples:
                    if curr[1] < range_end or curr[0] > range_start:
                        continue
                    elif range_start <= curr[0] <= curr[1] <= range_end:
                        offset = curr[0] - range_start
                        break
                    elif curr[0] < range_start <= curr[1] <= range_end:
                        offset = curr[1] - range_start
                        break
                    elif range_start <= curr[0] < range_end <= curr[1]:
                        offset = curr[0] - range_start
                        break
                    elif curr[0] < range_start <= range_end <= curr[1]:
                        pass
                else:
                    result.append(curr)
            remain = result
            result = []

    
part1()
part2()