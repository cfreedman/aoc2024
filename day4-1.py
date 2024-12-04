import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day4")

def main():
    characters = []
    with open(file_path) as f:
        for line in f:
            characters.append(list(line.rstrip()))
    
    rows, cols = len(characters), len(characters[0])
    return

if __name__ == "__main__":
    main()