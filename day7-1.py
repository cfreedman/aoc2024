import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day7")

def valid_test(value, nums):
    def dfs(index, computed_value):
        if index >= len(nums):
            return computed_value == value
        
        add_num = dfs(index + 1, computed_value + nums[index])
        multiply_num = dfs(index + 1, computed_value * nums[index])

        return add_num or multiply_num
    
    return dfs(1, nums[0])

total = 0

with open(file_path) as f:
    for line in f:
        test_value, nums = line.split(":")
        test_value = int(test_value)
        nums = [int(num) for num in nums.strip().split(" ")]
        total += test_value if valid_test(test_value, nums) else 0

print(total)
