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

grid = data.splitlines()
width = len(grid[0])
length = len(grid)

accessible = 0
# import pudb;pu.db
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

        accessible += paper <= 3 and grid[y][x] == "@"
    #     if paper <= 3 and grid[y][x] == "@":
    #         print("x", end="")
    #     else:
    #         print(grid[y][x], end="")
    # print()

submit(accessible)
