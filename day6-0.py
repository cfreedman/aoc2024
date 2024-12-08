import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day6")

def main():
    grid = []
    with open(file_path) as f:
        for line in f:
            grid.append(list(line.rstrip()))
    
    print(grid)
    return grid

if __name__ == "__main__":
    main()