from collections import deque
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day12")

farm = []
with open(file_path) as f:
    for line in f:
        farm.append(list(line.rstrip()))

directions = [[1,0],[-1,0],[0,1],[0,-1]]

def explore_region(row, col, farm, visited):
    rows, cols = len(farm), len(farm[0])
    q = deque([(row,col)])
    visited.add((row,col))
    perimeter = area = 0

    while q:
        length = len(q)
        for i in range(length):
            r, c = q.popleft()
            area += 1
            plot_perimeter = 0
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (
                    new_r < 0 or
                    new_r >= rows or
                    new_c < 0 or
                    new_c >= cols or
                    farm[new_r][new_c] != farm[row][col]
                ):
                    plot_perimeter += 1
                elif (new_r,new_c) not in visited:
                    q.append((new_r,new_c))
                    visited.add((new_r,new_c))
            perimeter += plot_perimeter
    
    return perimeter, area

def fence_price(farm):
    rows, cols = len(farm), len(farm[0])
    visited = set()

    total = 0
    for i in range(rows):
        for j in range(cols):
            if (i,j) in visited:
                continue

            perimeter,area = explore_region(i,j,farm,visited)
            total += perimeter*area

    return total

print(fence_price(farm))

def test1():
    farm = [[1,2],[1,1]]
    visited = set()

    perimeter, area = explore_region(0,0,farm,visited)
    print(perimeter, area)
    assert perimeter == 8 and area == 3

test1()
