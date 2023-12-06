from utils.api import get_input

input_str = get_input(6)

# WRITE YOUR SOLUTION HERE

times = [46,68,98,66]
distances = [358,1054,1807,1080]

def part1():
    solution = 1
    for i in range(4):
        count = 0
        for t in range(1,times[i]):
            t_temp = distances[i] / t
            if t_temp + t < times[i]:
                count += 1
        solution *= count
    print(solution)

def part2():
    temp1 = ""
    temp2 = ""
    for i in range(4):
        temp1 += str(times[i])
        temp2 += str(distances[i])
    time = int(temp1)
    distance = int(temp2)

    count = 0
    for t in range(1,time):
        t_temp = distance / t
        if t_temp + t <= time:
            count += 1
    print(count)

part1()
part2()