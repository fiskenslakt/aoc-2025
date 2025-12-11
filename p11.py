from collections import deque

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

data = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

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

# print("Part 1:", paths)
