from collections import deque
from functools import cache

from aocd import data


@cache
def dfs(device, visit_dac, visit_fft):
    if device == "out" and visit_dac and visit_fft:
        return 1
    elif device == "out":
        return 0

    paths = []

    for output in graph[device]:
        if output == "dac":
            paths.append(dfs(output, True, visit_fft))
        elif output == "fft":
            paths.append(dfs(output, visit_dac, True))

        paths.append(dfs(output, visit_dac, visit_fft))

    return sum(paths)


graph = {}

for line in data.splitlines():
    device, outputs = line.split(":")

    graph[device] = [output for output in outputs.split()]

queue = deque(["you"])
paths = 0

while queue:
    device = queue.popleft()

    if device == "out":
        paths += 1
        continue

    for output in graph[device]:
        queue.append(output)

print("Part 1:", paths)
print("Part 2:", dfs("svr", False, False))
