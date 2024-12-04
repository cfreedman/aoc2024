import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day1")

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
    right_index = 0
    for left_index in range(len(left_column)):
        curr_num = left_column[left_index]
        freq = 0

        while right_column[right_index] < curr_num:
            right_index += 1
        
        while right_column[right_index] == curr_num:
            freq += 1
            right_index += 1
        
        total += freq * curr_num

    print(total)
    return total


if __name__ == "__main__":
    main()

