import numpy as np
import os
import re

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "inputs/day13")

def isinteger(x):
    return np.equal(np.mod(x,1), 0)

class ClawMachine:
    def __init__(self,a,b,prize):
        self.a = a
        self.b = b
        self.prize = prize
    
    def find_cheapest(self):
        cheapest = float('inf')
        if self.prize[0] % self.a[0] == 0 and self.prize[1] % self.a[1] == 0 and self.prize[0] // self.a[0] == self.prize[1] // self.a[1]:
            cheapest = min(cheapest, 3 * (self.prize[0] // self.a[0]))
        if self.prize[0] % self.b[0] == 0 and self.prize[1] % self.b[1] == 0 and self.prize[0] // self.b[0] == self.prize[1] // self.b[1]:
            cheapest = min(cheapest, (self.prize[0] // self.b[0]))

        matrix = np.matrix([[self.a[0],self.b[0]],[self.a[1],self.b[1]]])
        b = np.matrix([[self.prize[0]], [self.prize[1]]])
        try:
            solution = np.linalg.solve(matrix,b)
            if isinteger(solution).all():
                cheapest = min(cheapest, 3 * solution[0,0] + solution[1,0])
        except np.linalg.LinAlgError:
            print("Singular matrix")

        return cheapest if cheapest != float('inf') else -1

total = 0

with open(file_path) as f:
    full_input = "".join(f.readlines())
    a_search = re.findall(r"Button A: X\+(\d+), Y\+(\d+)", full_input)
    b_search = re.findall(r"Button B: X\+(\d+), Y\+(\d+)", full_input)
    prize_search = re.findall(r"Prize: X=(\d+), Y=(\d+)", full_input)

    for a,b,prize in zip(a_search,b_search,prize_search):
        a = (int(a[0]), int(a[1]))
        b = (int(b[0]), int(b[1]))
        prize = (int(prize[0]), int(prize[1]))
        machine = ClawMachine(a,b,prize)

print(total)

def test1():
    a = (1,1)
    b = (3,3)
    prize = (2,2)

    machine = ClawMachine(a,b,prize)
    print(machine.find_cheapest())
    assert machine.find_cheapest() == 8

test1()




