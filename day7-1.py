import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day7")

def generate_results(nums):
    return dfs(nums, 1, nums[0])

def dfs(nums, curr_index, computed_value):
    if curr_index > len(nums) - 1:
        return [computed_value]
    
    add_results = dfs(nums, curr_index + 1, computed_value + nums[curr_index])
    multiply_results = dfs(nums, curr_index + 1, computed_value * nums[curr_index])
    concatenate_results = dfs(nums, curr_index + 1, int(str(computed_value) + str(nums[curr_index])))

    return add_results + multiply_results + concatenate_results

total = 0

with open(file_path) as f:
    for line in f:
        test_value, nums = line.split(":")
        test_value = int(test_value)
        nums = [int(num) for num in nums.strip().split(" ")]
        total += test_value if test_value in generate_results(nums) else 0

print(total)


def test_single_value():
    nums = [0]

    assert [0] == generate_results(nums)

def test_double_value():
    nums = [1, 2]

    assert generate_results(nums) == [3, 2, 12]

def test_triple_value():
    nums = [1,3,2]

    assert generate_results(nums) == [6,8,42,5,6,32,15,26,132]

test_single_value()
test_double_value()
test_triple_value()

