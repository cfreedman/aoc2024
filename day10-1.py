import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day10")

trail_map = []
with open(file_path) as f:
    for line in f:
        trail_map.append([int(num) for num in list(line.rstrip())])

rows, cols = len(trail_map), len(trail_map[0])
directions = [[0,1], [0,-1], [1,0], [-1,0]]

def trailhead_score(trail_map, row, col):
    rows, cols = len(trail_map), len(trail_map[0])

    if trail_map[row][col] == 9:
        return 1
    
    score = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and trail_map[new_row][new_col] == 1 + trail_map[row][col]:
            score += trailhead_score(trail_map, new_row, new_col)
    return score

total_score = 0

for i in range(rows):
    for j in range(cols):
        if trail_map[i][j] != 0:
            continue

        total_score += trailhead_score(trail_map, i, j)

print(total_score)




