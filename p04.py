from aocd import data, submit

# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

grid = [list(line) for line in data.splitlines()]
width = len(grid[0])
length = len(grid)

accessible = 0
removed = 0
# import pudb;pu.db

while True:
    new_grid = grid.copy()
    for y in range(width):
        for x in range(length):
            if grid[y][x] != "@":
                continue

            paper = 0
            for i in (-1, 0, 1):
                if paper >= 4:
                    break
                for j in (-1, 0, 1):
                    if i == j == 0:
                        continue
                    if paper >= 4:
                        break

                    nx = x + i
                    ny = y + j

                    if nx < 0 or nx >= width:
                        continue
                    if ny < 0 or ny >= length:
                        continue

                    if grid[ny][nx] == "@":
                        paper += 1

            if paper <= 3 and grid[y][x] == "@":
                accessible += 1
                new_grid[y][x] = "."

    grid = new_grid
    removed += accessible
    if accessible == 0:
        break
    else:
        accessible = 0

# print(accessible)
submit(removed)
