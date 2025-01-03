import os
import re

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day3")

def main():
    str = ""
    with open(file_path) as f:
        for line in f:
            str += line.strip()

    total = 0
    enabled = True
    for i, match in enumerate(re.finditer(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', str)):
        if match.group() == "do()":
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        elif enabled:
            left_num, right_num = match.group().strip("mul()").split(",")
            total += int(left_num) * int(right_num)
    print(total)
    return total

if __name__ == "__main__":
    main()