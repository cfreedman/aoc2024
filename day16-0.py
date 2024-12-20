import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day16")

maze = []
with open(file_path) as f:
    for line in f:
        maze.append(list(line.rstrip()))

def facing_to_direction(facing):
    if facing == "^":
        return [-1,0]
    if facing == ">":
        return [0,1]
    if facing == "v":
        return [1,0]
    return [0,-1]

def turn_facing(facing, counterclockwise):
    if facing == "^":
        return "<" if counterclockwise else ">"
    if facing == ">":
        return "^" if counterclockwise else "v"
    if facing == "v":
        return ">" if counterclockwise else "<"
    return "v" if counterclockwise else "^"

def opposite_facing(facing):
    if facing == "^":
        return "v"
    if facing == ">":
        return "<"
    if facing == "v":
        return "^"
    return ">"

class Maze:
    def __init__(self, maze):
        self.rows, self.cols = len(maze), len(maze[0])
        self.maze = maze
        self.reindeer_position = None
        self.reindeer_facing = None
        self.end = None
        self.scores_cache = {}

        for i in range(self.rows):
            for j in range(self.cols):
                if maze[i][j] == "S":
                    self.reindeer_position = (i,j)
                    self.reindeer_facing = ">" 
                elif maze[i][j] == "E":
                    self.end == (i,j)

    def calculate_lowest_score(self, curr_pos, curr_facing):
        if curr_pos == self.end:
            return 0
        if (curr_pos, curr_facing) in self.scores_cache:
            return self.scores_cache[(curr_pos, curr_facing)]
        
        visited = set()
        def dfs_traversal(curr_pos, curr_facing):
            if (curr_pos, curr_facing) in visited or (curr_pos, opposite_facing(curr_facing)) in visited:
                return float('inf')
            
            forward = clockwise = counterclockwise = float("inf")
            r,c = curr_pos
            dr,dc = facing_to_direction(curr_facing)
            if self.maze[r + dr][c + dc] != "#" and ((r + dr, c + dc), curr_facing) not in visited:
                forward = dfs_traversal((r + dr, c + dc), curr_facing)
            if 
            


    
reindeer_maze = Maze(maze)
print(reindeer_maze.calculate_lowest_score(reindeer_maze.reindeer_position, reindeer_maze.reindeer_facing))





