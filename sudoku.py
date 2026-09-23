from z3 import *

cells = [[Int(f'cell_{r}_{c}') for c in range(9)] for r in range(9)]

s = Solver()

for r in range(9):
    for c in range(9):
        s.add(And(cells[r][c] >= 1, cells[r][c] <= 9))

for r in range(9):
    s.add(Distinct(cells[r]))

for c in range(9):
    column = [cells[r][c] for r in range(9)]
    s.add(Distinct(column))

for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        box = [cells[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
        s.add(Distinct(box))

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

for r in range(9):
    for c in range(9):
        if puzzle[r][c] != 0:
            s.add(cells[r][c] == puzzle[r][c])

if s.check() == sat:
    m = s.model()

    for r in range(9):
        row = [m.evaluate(cells[r][c]) for c in range(9)]
        print(row)
else:
    print("No solution exists")