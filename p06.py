from operator import mul, add
from functools import reduce

from aocd import data, submit

# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """

problem_sheet = [line.split() for line in data.splitlines()]
problems = list(zip(*problem_sheet))
grand_total = 0

for problem in problems:
    *operands, operator = problem

    op = add if operator == "+" else mul
    grand_total += reduce(op, map(int, operands))

submit(grand_total)
