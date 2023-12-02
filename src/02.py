from utils.api import get_input
import re

input_str = get_input(2)

def part1():
    dic = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    pattern = re.compile('[\d]+ [\w]+')
    sum_ids = 0
    total_lines = 0
    for i,line in enumerate(input_str.splitlines(), start=1):
        a = pattern.findall(line)
        total_lines += i
        for j in a:
            n = j.split(" ")
            if int(n[0]) > dic[n[1]]:
                sum_ids += i
                break
    print(total_lines - sum_ids)

def part2():
    pattern = re.compile('[\d]+ [\w]+')
    total_sum = 0
    for line in input_str.splitlines():
        pairs = pattern.findall(line)
        # find the maximum of each color in each game
        dic = {
            "blue": 0,
            "green": 0,
            "red": 0
        }
        for p in pairs:
            n = p.split(" ")
            dic[n[1]] = max(dic[n[1]], int(n[0]))
        # multiply all the values to obtain the power
        col_mul = 1
        for k in dic.keys():
            col_mul *= dic[k]
        # sum to the total
        total_sum += col_mul
    print(total_sum)
        

if __name__ == "__main__":
    part1()
    part2()