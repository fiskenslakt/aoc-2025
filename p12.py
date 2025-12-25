from aocd import data

*gift_shapes, grids = data.split("\n\n")

gift_areas = [gift_shape.count("#") for gift_shape in gift_shapes]

valid_regions = 0

for grid in grids.splitlines():
    grid_area_raw, gift_counts_raw = grid.split(": ")

    grid_width, grid_height = map(int, grid_area_raw.split("x"))
    grid_area = grid_width * grid_height

    total_gift_area = 0
    for gift_idx, gift_count in enumerate(gift_counts_raw.split()):
        total_gift_area += gift_areas[gift_idx] * int(gift_count)

    if grid_area >= total_gift_area:
        valid_regions += 1

print("Part 1:", valid_regions)
print("Part 2: Merry Christmas!")
