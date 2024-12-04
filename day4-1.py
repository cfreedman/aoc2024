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
            if valid_xmas_block(characters, row, col):
                total += 1
    print(total)
    return total

def valid_xmas_block(grid, row, col):
    rows, cols = len(grid), len(grid[0])

    if row > rows - 3 or col > cols - 3:
        return False
    
    top_left_string = "".join([grid[row + i][col + i] for i in range(3)])
    bottom_left_string = "".join([grid[row + 2 - i][col + i] for i in range(3)])

    return (top_left_string == "MAS" or top_left_string == "SAM") and (bottom_left_string == "MAS" or bottom_left_string == "SAM")
    

if __name__ == "__main__":
    main()