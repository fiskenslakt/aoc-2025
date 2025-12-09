from itertools import combinations

from aocd import data, submit

# data = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3"""


def area(x1, y1, x2, y2):
    length = abs(y2 - y1) + 1
    width = abs(x2 - x1) + 1
    return length * width


tiles = [tuple(map(int, tile.split(","))) for tile in data.splitlines()]
largest_area = 0

for (x1, y1), (x2, y2) in combinations(tiles, 2):
    largest_area = max(largest_area, area(x1, y1, x2, y2))

submit(largest_area)
