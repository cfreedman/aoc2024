import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day6")

def main():
    grid = []
    with open(file_path) as f:
        for line in f:
            grid.append(list(line.rstrip()))
    
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "^>v<":
                position = (r, c)
                if grid[r][c] == "^":
                    pointing = "up"
                elif grid[r][c] == ">":
                    pointing = "right"
                elif grid[r][c] == "v":
                    pointing = "down"
                else:
                    pointing = "left"

                break
    
    path, _ = calculating_path(position, pointing, grid)
    
    loop_obstacles = set()
    for path_position, path_direction in path:
        next_r, next_c = next_position(path_position, path_direction)
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] != "#":
            altered_grid = [row[:] for row in grid]
            altered_grid[next_r][next_c] = "#"

            _, contains_loop = calculating_path(position, pointing, altered_grid)
            if contains_loop:
                loop_obstacles.add((next_r, next_c))

    print(len(loop_obstacles))

def calculating_path(start, pointing, grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    path = []

    position = start
    while 0 <= position[0] < rows and 0 <= position[1] < cols:
        if (position, pointing) in visited:
            return path, True
        visited.add((position, pointing))
        path.append((position, pointing))
        next_r, next_c = next_position(position, pointing)
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == "#":
            pointing = right_turn(pointing)
            continue

        position = next_position(position, pointing)
    
    return path, False
    
def right_turn(pointing):
    if pointing == "up":
        return "right"
    if pointing == "right":
        return "down"
    if pointing == "down":
        return "left"
    return "up"

def next_position(position, pointing):
    r, c = position
    if pointing == "up":
        return (r - 1, c)
    if pointing == "right":
        return (r, c + 1)
    if pointing == "down":
        return (r + 1, c)
    return (r, c - 1)

def grid_differences(grid1, grid2):
    differences = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid1[i][j] != grid2[i][j]:
                differences += 1
    
    return differences

if __name__ == "__main__":
    main()