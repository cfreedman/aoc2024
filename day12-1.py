from collections import deque
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day12")

farm = []
with open(file_path) as f:
    for line in f:
        farm.append(list(line.rstrip()))

directions = [[1,0],[-1,0],[0,1],[0,-1]]

def explore_region(row, col, farm, visited):
    rows, cols = len(farm), len(farm[0])
    q = deque([(row,col)])
    visited.add((row,col))
    region = set([(row,col)])

    while q:
        length = len(q)
        for _ in range(length):
            r, c = q.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (
                    new_r < 0 or
                    new_r >= rows or
                    new_c < 0 or
                    new_c >= cols or
                    farm[new_r][new_c] != farm[row][col]
                ):
                    continue
                elif (new_r,new_c) not in visited:
                    q.append((new_r,new_c))
                    visited.add((new_r,new_c))
                    region.add((new_r,new_c))
    
    return region

def get_edges(region):
    edges = set()

    for row, col in region:
        for dr, dc in directions:
            if (row + dr, col + dc) in region:
                continue

            edges.add(((row + (dr/2), col + (dc/2)), (dr/2, dc/2)))

    return edges

def get_sides(region):
    edges = get_edges(region)
    sides = 0

    visited = set()

    for edge, facing in edges:
        if (edge, facing) in visited:
            continue
        
        sides += 1
        visited.add((edge,facing))
        r_facing, c_facing = facing
        r_edge, c_edge = edge

        if c_facing == 0: # Edge extends along row facing up or down
            pos_idx = neg_idx = 0
            while ((r_edge, c_edge + pos_idx), facing) in edges:
                visited.add(((r_edge, c_edge + pos_idx), facing))
                pos_idx += 1
            
            
            while ((r_edge, c_edge - neg_idx), facing) in edges:
                visited.add(((r_edge, c_edge - neg_idx), facing))
                neg_idx += 1
            
        else: # Edge extends along column facing left or right
            pos_idx = neg_idx = 0
            while ((r_edge + pos_idx, c_edge), facing) in edges:
                visited.add(((r_edge + pos_idx, c_edge), facing))
                pos_idx += 1


            
            while ((r_edge - neg_idx, c_edge), facing) in edges:
                visited.add(((r_edge - neg_idx, c_edge), facing))
                neg_idx += 1


    return sides


def solve(farm):
    rows, cols = len(farm), len(farm[0])
    visited = set()
    total = 0

    for i in range(rows):
        for j in range(cols):
            if (i,j) in visited:
                continue

            region = explore_region(i,j,farm,visited)

            area = len(region)
            sides = get_sides(region)

            print(region)
            print(area)
            print(sides)

            total += area * sides

    return total

print(solve(farm))

def edges_test():
    region = set([(0,0),(1,0),(0,1)])

    print(get_edges(region))

def sides_test():
    region = set([(0,0),(1,0),(0,1)])

    print(get_sides(region))

sides_test()

def farm_test():
    farm = [["A","B","B"],["C","D","B"],["C","C","E"]]

    print(solve(farm))

