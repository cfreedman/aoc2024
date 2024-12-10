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
        
    visited = set()
    
    while 0 <= position[0] < rows and 0 <= position[1] < cols:
        if position not in visited:
            visited.add(position)
        next_r, next_c = next_position(position, pointing)
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == "#":
            pointing = right_turn(pointing)
            continue

        position = next_position(position, pointing)

    print(len(visited))

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

if __name__ == "__main__":
    main()