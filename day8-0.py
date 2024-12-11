from collections import defaultdict
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

            if 0 <= r2 + row_gap < rows and 0 <= c2 + col_gap < cols:
                antinode_positions.add((r2 + row_gap, c2 + col_gap))
            
            if 0 <= r1 - row_gap < rows and 0 <= c1 - col_gap < cols:
                antinode_positions.add((r1 - row_gap, c1 - col_gap))

print(len(antinode_positions))

