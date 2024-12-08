import collections
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day5")

def main():
    with open(file_path) as f:
        ordering = collections.defaultdict(list)
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
                ordering[num].append(prereq)


    total = 0
    for update in updates:
        valid = True
        for i, num in enumerate(update):
            if any([num in ordering[prev] for prev in update[:i]]):
                valid = False
                break
        
        total += int(update[len(update) // 2]) if valid else 0
    
    print(total)
    return total

if __name__ == "__main__":
    main()