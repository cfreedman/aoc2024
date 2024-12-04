import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day1-0")


def main():
    left_column, right_column = [], []
    with open(file_path) as f:
        for line in f:
            left_num, right_num = line.split()
            left_column.append(int(left_num))
            right_column.append(int(right_num))

    left_column.sort()
    right_column.sort()

    total = 0
    for left_num, right_num in zip(left_column, right_column):
        total += abs(left_num - right_num)
    
    print(total)
    return total

if __name__ == "__main__":
    main()
