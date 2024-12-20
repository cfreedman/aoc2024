import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day9")

def generate_full_disk_map(disk_map):
    fill_segs = []
    spaces = []

    fill = True
    id = 0
    curr_idx = 0

    for num in disk_map:
        num = int(num)
        if fill:
            fill_segs.append([curr_idx, curr_idx + num])
            fill = False
        else:
            spaces.append([curr_idx, curr_idx + num])
            fill = True
        curr_idx += num
    
    return fill_segs, spaces

def shift_file_blocks(disk_map):
    fill_segs, spaces = generate_full_disk_map(disk_map)

    for i in range(len(fill_segs) - 1,-1,-1):
        start, end = fill_segs[i]
        seg_length = end - start
        j = 0
        while spaces[j][0] < start:
            space_start, space_end = spaces[j]
            space_length = space_end - space_start
            if space_length >= seg_length:
                fill_segs[i] = [space_start, space_start + seg_length]
                new_space_start = space_start + seg_length
                if space_end - new_space_start == 0:
                    spaces.pop(j)
                else:
                    spaces[j][0] = new_space_start
                break
            j += 1
    
    return fill_segs, spaces

def checksum(fill_segs):
    checksum = 0

    for i in range(len(fill_segs)):
        start, end = fill_segs[i]
        checksum += sum([i*idx for idx in range(start, end)])
    
    return checksum

with open(file_path) as f:
    disk_map = [int(num) for num in list(f.read().strip())]
    shifted_segs, _ = shift_file_blocks(disk_map)
    print(checksum(shifted_segs))

def test1():
    disk_map = [1,2,3]

    fill_segs, spaces = generate_full_disk_map(disk_map)
    assert fill_segs == [[0,1],[3,6]] and spaces == [[1,3]]

def test2():
    disk_map = [1,3,2]

    fill_segs, spaces = shift_file_blocks(disk_map)
    assert fill_segs == [[0,1],[1,3]] and spaces == [[3,4]]

test1()
test2()