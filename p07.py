from collections import deque

from aocd import data, submit

# data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

manifold = {}
emitter = None

for y, line in enumerate(data.splitlines()):
    for x, cell in enumerate(line):
        if cell == "S":
            emitter = (x, y)

        manifold[(x, y)] = cell

queue = deque([emitter])
hit_splitters = set()
seen_beams = set()
# import pudb;pu.db
while queue:
    x, y = queue.popleft()

    while (x, y) in manifold:
        y += 1

        if (x, y) in manifold:
            if manifold[(x, y)] == ".":
                manifold[(x, y)] = "|"
                seen_beams.add((x, y))
            elif manifold[(x, y)] == "^": # and (x, y) not in hit_splitters:
                hit_splitters.add((x, y))
                manifold[(x-1, y)] = "|"
                if (x-1, y) not in seen_beams:
                    queue.append((x-1, y))
                    seen_beams.add((x-1, y))
                manifold[(x+1, y)] = "|"
                if (x+1, y) not in seen_beams:
                    queue.append((x+1, y))
                    seen_beams.add((x+1, y))
                break

# print(sum(cell == "|" for cell in manifold.values()))
submit(len(hit_splitters))
# for y, line in enumerate(data.splitlines()):
#     for x, _ in enumerate(line):
#         print(manifold[(x, y)], end="")
#     print()
