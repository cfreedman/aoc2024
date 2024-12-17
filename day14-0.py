import os
import re

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day14")

rows, cols = 103, 101

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def next_position(self):
        next_row = (self.position[1] + self.velocity[1]) % rows
        next_col = (self.position[0] + self.velocity[0]) % cols

        return (next_col,next_row)
    
    def simulate_movement(self, turns):

        for _ in range(turns):
            self.position = self.next_position()

grid = [[0]*cols for _ in range(rows)]
top_left_count = 0
top_right_count = 0
bottom_left_count = 0
bottom_right_count = 0

with open(file_path) as f:
    for line in f:
        position_search = re.search(r"p=(\d+),(\d+)", line)
        velocity_search = re.search(r"v=(-?\d+),(-?\d+)", line)
        if position_search:
            position = (int(position_search.group(1)), int(position_search.group(2)))
        if velocity_search:
            velocity = (int(velocity_search.group(1)), int(velocity_search.group(2)))
        robot = Robot(position, velocity)
        robot.simulate_movement(100)
        if robot.position[0] == 50 or robot.position[1] == 51:
            continue

        if robot.position[0] < 50 and robot.position[1] < 51:
            top_left_count += 1
        elif robot.position[0] > 50 and robot.position[1] < 51:
            top_right_count += 1
        elif robot.position[0] < 50 and robot.position[1] > 51:
            bottom_left_count += 1
        else:
            bottom_right_count += 1

print(top_left_count, top_right_count, bottom_left_count, bottom_right_count)
print(top_left_count*top_right_count*bottom_left_count*bottom_right_count)

def test_parsing():
    test_string = "p=4,5 v=4,6"
    position_search = re.search(r"p=(\d+),(\d+)", test_string)
    velocity_search = re.search(r"v=(\d+),(\d+)", test_string)

    position = (int(position_search.group(1)), int(position_search.group(2)))
    velocity = (int(velocity_search.group(1)), int(velocity_search.group(2)))

    assert position == (4,5) and velocity == (4,6)

def test_robot_movement():
    robot = Robot((1,1),(-1,2))

    assert robot.next_position() == (0,3)

def test_robot_loop():
    robot = Robot((1,1),(-1,2))
    robot.simulate_movement(3)

    assert robot.position == (99,7)

test_parsing()
test_robot_movement()
test_robot_loop()