import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day11")

stones = []
with open(file_path) as f:
    for line in f:
        stones.extend([int(num) for num in line.rstrip().split(" ")])

def transform_stones(stones):
    new_stones = []

    for num in stones:
        if num == 0:
            new_stones.append(1)
        elif len(str(num)) % 2 == 0:
            string_num = str(num)
            first_half = string_num[:(len(string_num) // 2)]
            second_half = string_num[(len(string_num) // 2):]

            first_half = int(first_half)
            second_half = int(second_half) if second_half != "0" * len(second_half) else 0
            new_stones.extend([first_half, second_half])
        else:
            new_stones.append(num * 2024)

    return new_stones

for _ in range(25):
    stones = transform_stones(stones)

print(len(stones))

def test1():
    stones = [125, 17]
    print(transform_stones(stones))
    assert transform_stones(stones) == [253000, 1, 7]

def test2():
    stones = [125, 17]

    for _ in range(2):
        stones = transform_stones(stones)
    print(stones)
    assert stones == [253, 0, 2024, 14168]

test1()
test2()