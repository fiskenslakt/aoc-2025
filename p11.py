from collections import deque
from functools import cache

from aocd import data, submit

# data = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out
# """

# data = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out
# """


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

# queue = deque(["you"])
# paths = 0

# while queue:
#     device = queue.popleft()

#     if device == "out":
#         paths += 1
#         continue

#     for output in graph[device]:
#         queue.append(output)

# print("Part 1:", paths)

# queue = deque([("svr", False, False)])
# paths = 0
# seen = set()

# while queue:
#     device, visit_dac, visit_fft = queue.popleft()

#     if device == "out" and visit_dac and visit_fft:
#         paths += 1
#         continue
#     elif device == "out":
#         continue

#     for output in graph[device]:
#         if output == "dac":
#             queue.append((output, True, visit_fft))
#         elif output == "fft":
#             queue.append((output, visit_dac, True))

#         if output not in seen:
#             queue.append((output, visit_dac, visit_fft))
#             seen.add(output)

# print(paths)
submit(dfs("svr", False, False))
