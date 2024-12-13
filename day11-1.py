import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day11")

stones = []
with open(file_path) as f:
    for line in f:
        stones.extend([int(num) for num in line.rstrip().split(" ")])

cache = dict()

def stones_after_blinks(curr_stone, blinks):
    if not blinks:
        return 1
    if (curr_stone, blinks) in cache:
        return cache[(curr_stone, blinks)]
    
    if curr_stone == 0:
        res = stones_after_blinks(1, blinks - 1)
    elif len(str(curr_stone)) % 2 == 0:
        string_num = str(curr_stone)
        first_half = string_num[:(len(string_num) // 2)]
        second_half = string_num[(len(string_num) // 2):]
        first_half = int(first_half)
        second_half = int(second_half)
        res = stones_after_blinks(first_half, blinks - 1) + stones_after_blinks(second_half, blinks - 1)
    else:
        res = stones_after_blinks(curr_stone * 2024, blinks - 1)

    cache[(curr_stone, blinks)] = res
    return res     

total = 0
for stone in stones:
    total += stones_after_blinks(stone, 75)

print(total)

def test1():

    res = stones_after_blinks(0, 2)
    assert res == 1

def test2():
    res = stones_after_blinks(0, 4)
    assert res == 4

def test3():
    nums = [125,17]
    total = 0
    for num in nums:
        total += stones_after_blinks(num, 6)

    assert total == 22

test1()
test2()
test3()