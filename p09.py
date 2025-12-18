from itertools import combinations

from aocd import data
from shapely import Polygon, box


def area(x1, y1, x2, y2):
    length = abs(y2 - y1) + 1
    width = abs(x2 - x1) + 1
    return length * width


tiles = [tuple(map(int, tile.split(","))) for tile in data.splitlines()]
polygon = Polygon(tiles)
largest_area = 0
largest_contained_area = 0

for (x1, y1), (x2, y2) in combinations(tiles, 2):
    largest_area = max(largest_area, area(x1, y1, x2, y2))

    rectangle = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    if polygon.contains(rectangle):
        largest_contained_area = max(largest_contained_area, area(x1, y1, x2, y2))

print("Part 1:", largest_area)
print("Part 2:", largest_contained_area)
