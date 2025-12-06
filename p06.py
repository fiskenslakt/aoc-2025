from functools import reduce
from operator import add, mul

from aocd import data

problem_sheet = [line.split() for line in data.splitlines()]
problems = list(zip(*problem_sheet))
grand_total = 0

for problem in problems:
    *operands, operator = problem

    op = add if operator == "+" else mul
    grand_total += reduce(op, map(int, operands))

real_problem_sheet = list(zip(*data.splitlines()))[::-1]
real_grand_total = 0
i = 0
while i < len(real_problem_sheet):
    problem = []

    while i < len(real_problem_sheet) and not all(
        j == " " for j in real_problem_sheet[i]
    ):
        problem.append(real_problem_sheet[i])
        i += 1
    operator = problem[-1][-1]
    op = add if operator == "+" else mul

    operands = []
    for operand in problem:
        operands.append(int("".join(operand[:-1])))

    real_grand_total += reduce(op, operands)
    i += 1

print("Part 1:", grand_total)
print("Part 2:", real_grand_total)
