from collections import deque

from aocd import data

dial = deque(list(range(100)))
dial.rotate(50)
landed_on_zero = 0
passed_zero = 0

for line in data.splitlines():
    for _ in range(int(line[1:])):
        if line[0] == "L":
            dial.rotate(-1)
        else:
            dial.rotate(1)

        if dial[0] == 0:
            passed_zero += 1

    if dial[0] == 0:
        landed_on_zero += 1

print("Part 1:", landed_on_zero)
print("Part 2:", passed_zero)
