import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day4")

def main():
    characters = []
    with open(file_path) as f:
        for line in f:
            characters.append(list(line.rstrip()))
    
    rows, cols = len(characters), len(characters[0])
    total = 0
    for row in range(rows):
        for col in range(cols):
            total += valid_xmas_number(characters, row, col)
    print(total)
    return total

def valid_xmas_number(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]

    if grid[row][col] != "X":
        return 0
    
    total = 0

    for dr, dc in directions:
        matching_char = "M"
        index = 0
        r, c = row, col
        while index < 3:
            r, c = r + dr, c + dc
            if 0 > r or r >= rows or 0 > c or c >= cols or grid[r][c] != matching_char:
                break
            
            if index == 0:
                matching_char = "A"
            elif index == 1:
                matching_char = "S"
            index += 1
        
        if index == 3:
            total += 1
            
    return total

if __name__ == "__main__":
    grid = [["X", "M", "A", "S"]]
    print("test")
    print(valid_xmas_number(grid, 0, 0))
    main()
