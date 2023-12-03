from utils.api import get_input
import numpy as np

input_str = get_input(3)
lines = input_str.splitlines()

n = len(lines[0])
m = len(lines)

directions_sym = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1, 1), (1,-1), (-1,-1)]

def part1():
    mat = [ [ 0 for i in range(n) ] for j in range(m) ]
    for i in range(m):
        for j in range(n):
            mat[i][j] = lines[i][j]

    total_sum = 0
    for y in range(m):
        for x in range(n):
            if mat[y][x] != "." and not mat[y][x].isnumeric():
                # found a symbol
                for d in directions_sym:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if new_y < m and new_x < n and mat[new_y][new_x].isnumeric():
                        # find the start
                        start_n = new_x - 1
                        while True:
                            if start_n < 0 or not mat[new_y][start_n].isnumeric():
                                break
                            start_n -= 1
                        start_n += 1
                        
                        # same with the end
                        end_n = new_x + 1
                        while True:
                            if end_n >= n or not mat[new_y][end_n].isnumeric():
                                break
                            end_n += 1

                        number = ''.join(mat[new_y][start_n:end_n])
                        for i in range(start_n, end_n):
                            mat[new_y][i] = "."

                        total_sum += int(number)

    print("part 1: ", total_sum)

def part2():
    mat = [ [ 0 for i in range(n) ] for j in range(m) ]
    for i in range(m):
        for j in range(n):
            mat[i][j] = lines[i][j]

    total_sum = 0
    for y in range(m):
        for x in range(n):
            if mat[y][x] == "*":
                numbers = []
                for d in directions_sym:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if new_y < m and new_x < n and mat[new_y][new_x].isnumeric():
                        # find the start
                        start_n = new_x - 1
                        while True:
                            if start_n < 0 or not mat[new_y][start_n].isnumeric():
                                break
                            start_n -= 1
                        start_n += 1
                        
                        # same with the end
                        end_n = new_x + 1
                        while True:
                            if end_n >= n or not mat[new_y][end_n].isnumeric():
                                break
                            end_n += 1

                        number = ''.join(mat[new_y][start_n:end_n])
                        for i in range(start_n, end_n):
                            mat[new_y][i] = "."
                        numbers.append(number)
                    
                gear = 0
                if len(numbers) == 2:
                    gear = int(numbers[0]) * int(numbers[1])
                total_sum += gear

    print("part 2:", total_sum)

part1()
part2()