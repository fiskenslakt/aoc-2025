from itertools import combinations

from aocd import data, submit


joltage = 0

for bank in data.splitlines():
    bat = max(combinations(map(int, bank), 2))
    joltage += int("".join(map(str, bat)))

print("Part 1:", joltage)
