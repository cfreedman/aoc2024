import heapq
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day16")

maze = []
with open(file_path) as f:
    for line in f:
        maze.append(list(line.rstrip()))

rows, cols = len(maze), len(maze[0])

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == "S":
            start = (i,j)
        if maze[i][j] == "E":
            end = (i,j)

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

def lowest_score(maze, curr_pos, curr_facing):
    visited = {(curr_pos, ">"): 0}
    heap = [(0, curr_pos, curr_facing)]
    heapq.heapify(heap)
    score = float('inf')

    while heap:
        curr_score, curr_pos, curr_facing = heapq.heappop(heap)
        r, c = curr_pos
        if maze[r][c] == "E":
            return curr_score
        dr, dc = facing_to_direction(curr_facing)
        if (maze[r + dr][c + dc] != "#" and ((r + dr, c + dc), curr_facing) not in visited) or (((r + dr, c + dc), curr_facing) in visited and visited[((r + dr, c + dc), curr_facing)] > curr_score + 1):
            heapq.heappush(heap, (curr_score + 1, (r + dr, c + dc), curr_facing))
            visited[((r + dr, c + dc), curr_facing)] = curr_score + 1
        if (curr_pos, turn_facing(curr_facing, True)) not in visited or visited[(curr_pos, turn_facing(curr_facing, True))] > curr_score + 1000:
            heapq.heappush(heap, (curr_score + 1000, curr_pos, turn_facing(curr_facing, True)))
            visited[((r, c), turn_facing(curr_facing, True))] = curr_score + 1000
        if (curr_pos, turn_facing(curr_facing, False)) not in visited or visited[(curr_pos, turn_facing(curr_facing, False))] > curr_score + 1000:
            heapq.heappush(heap, (curr_score + 1000, curr_pos, turn_facing(curr_facing, False)))
            visited[((r, c), turn_facing(curr_facing, False))] = curr_score + 1000

    return score

def find_best_path_tiles(maze, curr_pos, curr_facing):
    lowest = lowest_score(maze, curr_pos, curr_facing)
    visited = {(curr_pos, curr_facing): 0}
    heap = [(0, curr_pos, curr_facing, set([curr_pos]))]
    heapq.heapify(heap)

    best_positions = set()

    while heap:
        curr_score, curr_pos, curr_facing, positions_so_far = heapq.heappop(heap)
        if curr_score > lowest:
            continue
        r, c = curr_pos

        if maze[r][c] == "E":
            print("Adding one paths positions")
            best_positions = best_positions | positions_so_far
        dr, dc = facing_to_direction(curr_facing)
        if (maze[r + dr][c + dc] != "#" and ((r + dr, c + dc), curr_facing) not in visited) or (((r + dr, c + dc), curr_facing) in visited and visited[((r + dr, c + dc), curr_facing)] >= curr_score + 1):
            updated_positions = positions_so_far.copy()
            updated_positions.add((r + dr, c + dc))
            heapq.heappush(heap, (curr_score + 1, (r + dr, c + dc), curr_facing, updated_positions))
            visited[((r + dr, c + dc), curr_facing)] = curr_score + 1
        if (curr_pos, turn_facing(curr_facing, True)) not in visited or visited[(curr_pos, turn_facing(curr_facing, True))] >= curr_score + 1000:
            heapq.heappush(heap, (curr_score + 1000, curr_pos, turn_facing(curr_facing, True), positions_so_far.copy()))
            visited[((r, c), turn_facing(curr_facing, True))] = curr_score + 1000
        if (curr_pos, turn_facing(curr_facing, False)) not in visited or visited[(curr_pos, turn_facing(curr_facing, False))] >= curr_score + 1000:
            heapq.heappush(heap, (curr_score + 1000, curr_pos, turn_facing(curr_facing, False), positions_so_far.copy()))
            visited[((r, c), turn_facing(curr_facing, False))] = curr_score + 1000

    return best_positions

def draw_map(maze, best_positions):
    rows, cols = len(maze), len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if (i,j) in best_positions:
                maze[i][j] = "O"

    for i in range(rows):
        print("".join(maze[i]))
    
best_positions = find_best_path_tiles(maze, start, ">")
print(best_positions)
print(len(best_positions))

# draw_map(maze,best_positions)

def test_maze():
    maze = [["#","#","#","#","#"],["#",".","#","E","#"],["#",".",".",".","#"],["#",".",".",".","#"],["#",".","#","#","#"], ["#","#","#","#","#"]]

    print(find_best_path_tiles(maze,(4,1),">"))

# test_maze()
