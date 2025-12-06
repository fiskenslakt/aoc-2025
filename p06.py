from operator import mul, add
from functools import reduce

from aocd import data, submit

# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """


real_problem_sheet = list(zip(*data.splitlines()))[::-1]

# problem_sheet = [line.split(" ") for line in data.splitlines()]
# problems = list(zip(*problem_sheet))
# grand_total = 0

# for problem in problems:
#     *operands, operator = problem

#     op = add if operator == "+" else mul
#     grand_total += reduce(op, map(int, operands))

# submit(grand_total)
# import pudb# ;pu.db
grand_total = 0
i = 0
while i < len(real_problem_sheet):
    problem = []

    while i < len(real_problem_sheet) and not all(j == " " for j in real_problem_sheet[i]):
        problem.append(real_problem_sheet[i])
        i += 1
    operator = problem[-1][-1]
    op = add if operator == "+" else mul

    operands = []
    for operand in problem:
        operands.append(int("".join(operand[:-1])))

    grand_total += reduce(op, operands)

    i += 1

submit(grand_total)
