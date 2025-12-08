from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, count
from math import sqrt
from operator import mul

from aocd import data


def dist(p, q):
    p1, p2, p3 = p
    q1, q2, q3 = q
    return sqrt((p1 - q1) ** 2 + (p2 - q2) ** 2 + (p3 - q3) ** 2)


junction_boxes = [tuple(map(int, line.split(","))) for line in data.splitlines()]

box_distances = []
for box1, box2 in combinations(junction_boxes, 2):
    heappush(box_distances, (dist(box1, box2), (box1, box2)))

circuits = []

for connection in count(start=1):
    _, (box1, box2) = heappop(box_distances)

    changed_circuits = []
    for i, circuit in enumerate(circuits):
        if box1 in circuit or box2 in circuit:
            circuits[i].add(box1)
            circuits[i].add(box2)
            changed_circuits.append(circuit)

    if not changed_circuits:
        circuits.append({box1, box2})
    else:
        for changed_circuit in changed_circuits:
            circuits.remove(changed_circuit)
        circuits.append(reduce(set.union, changed_circuits))

    if connection == 1000:
        print(
            "Part 1:",
            reduce(mul, [len(c) for c in sorted(circuits, key=len, reverse=True)[:3]]),
        )
    elif len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
        print("Part 2:", box1[0] * box2[0])
        break
