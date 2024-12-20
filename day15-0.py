import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day15")


warehouse_map = []
instructions = ""
instructions_switch = False

with open(file_path) as f:
    for line in f:
        if line == "\n":
            instructions_switch = True
            continue
        
        if not instructions_switch:
            warehouse_map.append(list(line.rstrip()))
        else:
            instructions += line.rstrip()

def instruction_to_direction(instruction):
    if instruction == "^":
        return [-1,0]
    if instruction == ">":
        return [0,1]
    if instruction == "v":
        return [1,0]
    return [0,-1]

class Warehouse:

    def __init__(self, warehouse, instructions):
        self.warehouse = warehouse
        self.instructions = instructions

        self.rows, self.cols = len(warehouse), len(warehouse[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if self.warehouse[i][j] == "@":
                    self.robot_position = [i,j]
    
    def update_warehouse(self, instruction):
        dr, dc = instruction_to_direction(instruction)
        r, c = self.robot_position

        if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols and self.warehouse[r + dr][c + dc] == ".":
            print("Empty space in front")
            self.warehouse[r][c] = "."
            self.warehouse[r + dr][c + dc] = "@"
            self.robot_position = [r + dr, c + dc]
            return
        
        if self.warehouse[r + dr][c + dc] == "#":
            print("Wall directly in front")
            return
        
        obstacle_count = 1
        while self.warehouse[r + obstacle_count * dr][c + obstacle_count * dc] == "O":
            obstacle_count += 1
        
        if self.warehouse[r + obstacle_count * dr][c + obstacle_count * dc] == "#":
            print("Obstacles blocked by wall")
            return
        
        self.warehouse[r + obstacle_count * dr][c + obstacle_count * dc] = "O"
        self.warehouse[r + dr][c + dc] = "@"
        self.robot_position = [r + dr, c + dc]
        self.warehouse[r][c] = "."

    def execute_instructions(self):
        for instruction in self.instructions:
            self.update_warehouse(instruction)

    def calculate_gps_score(self):
        total = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.warehouse[i][j] == "O":
                    total += 100 * i + j
        print(total)
        return total
        


warehouse = Warehouse(warehouse_map,instructions)
warehouse.execute_instructions()
warehouse.calculate_gps_score()