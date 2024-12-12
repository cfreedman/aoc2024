from collections import defaultdict
from math import gcd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day8")

grid = []

with open(file_path) as f:
    for line in f:
        grid.append(list(line.rstrip()))

rows, cols = len(grid), len(grid[0])
antennas = defaultdict(list) 

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == ".":
            continue

        antennas[grid[row][col]].append((row,col))

antinode_positions = set()

for char in antennas.keys():
    positions = antennas[char]
    length = len(positions)
    for i in range(length):
        for j in range(i + 1, length):
            (r1, c1), (r2, c2) = positions[i], positions[j]
            row_gap, col_gap = r2 - r1, c2 - c1

            # Reduce row_gap and col_gap to their smallest factors
            row_gap, col_gap = row_gap // gcd(row_gap, col_gap), col_gap // gcd(row_gap, col_gap)

            antinode_positions.add((r1, c1))

            # Negative ray direction
            ray_index = 1
            while 0 <= r1 - ray_index * row_gap < rows and 0 <= c1 - ray_index * col_gap < cols:
                antinode_positions.add((r1 - ray_index * row_gap, c1 - ray_index * col_gap))
                ray_index += 1

            # Positive ray direction
            ray_index = 1
            while 0 <= r1 + ray_index * row_gap < rows and 0 <= c1 + ray_index * col_gap < cols:
                antinode_positions.add((r1 + ray_index * row_gap, c1 + ray_index * col_gap))
                ray_index += 1

print(len(antinode_positions))
