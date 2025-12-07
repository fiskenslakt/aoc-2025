from collections import deque
from functools import cache

from aocd import data


@cache
def emit_tachyon(x, y):
    if (x, y) not in manifold:
        return 1

    if manifold[(x, y)] == "^":
        return emit_tachyon(x - 1, y) + emit_tachyon(x + 1, y)

    return emit_tachyon(x, y + 1)


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

while queue:
    x, y = queue.popleft()

    while (x, y) in manifold:
        y += 1

        if (x, y) in manifold:
            if manifold[(x, y)] == ".":
                seen_beams.add((x, y))

            elif manifold[(x, y)] == "^":
                hit_splitters.add((x, y))

                if (x - 1, y) not in seen_beams:
                    queue.append((x - 1, y))
                    seen_beams.add((x - 1, y))

                if (x + 1, y) not in seen_beams:
                    queue.append((x + 1, y))
                    seen_beams.add((x + 1, y))

                break

print("Part 1:", len(hit_splitters))
print("Part 2:", emit_tachyon(*emitter))
