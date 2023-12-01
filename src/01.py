from utils.api import get_input

input_str = get_input(1)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def part1():
    solution = 0
    for line in input_str.splitlines():
        n = []
        for c in line:
            if c.isnumeric():
                n.append(c)
        solution += int(n[0] + n[len(n) - 1])

    print(solution)

def part2():
    dic = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10"
    }

    solution = 0
    for line in input_str.splitlines():
        n = []
        for word in dic.keys():
            i = find_all(line, word)
            for ind in i:
                if ind != -1:
                    n.append((ind, dic[word]))
        
        for j in range(len(line)):
            if line[j].isnumeric():
                n.append((j, line[j]))

        n.sort(key=lambda x : x[0])
        solution +=  int(n[0][1] + n[len(n) - 1][1])
    print(solution)


if __name__ == "__main__":
    part1()
    part2()