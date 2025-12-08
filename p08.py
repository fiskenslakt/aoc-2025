from operator import mul
from functools import reduce
from itertools import combinations, count
from heapq import heappush, heappop
from math import sqrt

from aocd import data, submit

# data = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""


def dist(p, q):
    p1, p2, p3 = p
    q1, q2, q3 = q
    return sqrt((p1 - q1)**2 + (p2 - q2)**2 + (p3 - q3)**2)


junction_boxes = [tuple(map(int, line.split(","))) for line in data.splitlines()]

box_distances = []
for box1, box2 in combinations(junction_boxes, 2):
    heappush(box_distances, (dist(box1, box2), (box1, box2)))

# import pudb# ;pu.db
# while box_distances:
circuits = []
for conn in count(start=1):
    _, (box1, box2) = heappop(box_distances)

    changed_circuits = []
    for i, circuit in enumerate(circuits):
        if box1 in circuit or box2 in circuit:
            circuits[i].add(box1)
            circuits[i].add(box2)
            changed_circuits.append(circuit)

    if not changed_circuits:
        circuits.append({box1, box2})
    # elif len(changed_circuits) == len(circuits) == 2:
    #     print("conn =", conn)
    #     print(box1, box2)
    #     print(box1[0] * box2[0])
    #     break
    else:
        for changed_circuit in changed_circuits:
            circuits.remove(changed_circuit)
        circuits.append(reduce(set.union, changed_circuits))

    if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
        # print(box1, box2)
        # print(conn)
        # print("ans:", box1[0] * box2[0])
        submit(box1[0] * box2[0])
        break

# for circuit in circuits:
#     print(len(circuit), circuit)

# print("Part 1:", reduce(mul, [len(c) for c in sorted(circuits, key=len, reverse=True)[:3]]))
