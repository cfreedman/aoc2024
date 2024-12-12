import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day9")


def shift_file_blocks(disk_map):
    left, right = 0, len(disk_map) - 1
    res = []

    while left <= right:
        if right % 2 != 0:
            right -= 1
            continue

        if left % 2 == 0:
            res.extend([left // 2] * disk_map[left])
            left += 1
            continue

        if disk_map[right] > disk_map[left]:
            res.extend([right // 2] * disk_map[left])
            disk_map[right] -= disk_map[left]
            left += 1
        elif disk_map[right] < disk_map[left]:
            res.extend([right // 2] * disk_map[right])
            disk_map[left] -= disk_map[right]
            right -= 1
        else:
            res.extend([right // 2] * disk_map[left])
            left += 1
            right -= 1
    
    return res

checksum = 0

with open(file_path) as f:
    for line in f:
        disk_map = [int(num) for num in list(line.rstrip())]
        shifted_disk_map = shift_file_blocks(disk_map)
        print(shifted_disk_map)
        checksum += sum([i * shifted_disk_map[i] for i in range(len(shifted_disk_map))])

print(checksum)

def test1():
    nums = [1,2,3,4,5]

    res = shift_file_blocks(nums)
    print(res)
    assert res == [0,2,2,1,1,1,2,2,2]

def test2():
    nums = [2,3,3,3,1,3,3,1,2,1,4,1,4,1,3,1,4,0,2]

    res = shift_file_blocks(nums)
    print(res)
    assert res == [0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6]

test1()
test2()
        