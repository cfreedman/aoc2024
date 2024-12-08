import collections
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day5")

def main():
    with open(file_path) as f:
        adjacency_list = collections.defaultdict(list)
        updates = []
        ordering_finished = False
        for line in f:
            if line.strip() == "":
                ordering_finished = True
                continue
            if ordering_finished:
                updates.append(line.rstrip().split(","))
            else:
                prereq, num = line.rstrip().split("|")
                adjacency_list[prereq].append(num)


    total = 0
    for update in updates:
        valid = True
        for i, num in enumerate(update):
            if any([prev in adjacency_list[num] for prev in update[:i]]):
                sub_adjacency_list = {prereq: [num for num in adjacency_list[prereq] if num in set(update)] for prereq in set(update)}
                corrected_update = topological_sort(sub_adjacency_list, update)
                total += int(corrected_update[len(corrected_update) // 2])
                break
    
    print(total)
    return total

def topological_sort(adjacency_list, values):
    stack = []
    visited = set()

    for num in values:
        if num not in visited:
            helper(num, adjacency_list, visited, stack)

    return stack[::-1]

def helper(curr, adjacency_list, visited, stack):
    visited.add(curr)

    for neighbor in adjacency_list[curr]:
        if neighbor not in visited:
            helper(neighbor, adjacency_list, visited, stack)
    
    stack.append(curr)

if __name__ == "__main__":
    main()