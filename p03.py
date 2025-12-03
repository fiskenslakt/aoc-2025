from aocd import data


def get_largest_joltage(bank, batteries, spots):
    if spots == 1:
        return batteries + max(bank)

    i, next_bat = max(enumerate(bank[: -spots + 1]), key=lambda b: (b[1], -b[0]))

    return get_largest_joltage(bank[i + 1 :], batteries + next_bat, spots - 1)


joltage_1 = 0
joltage_2 = 0

for bank in data.splitlines():
    joltage_1 += int(get_largest_joltage(bank, "", 2))
    joltage_2 += int(get_largest_joltage(bank, "", 12))

print("Part 1:", joltage_1)
print("Part 2:", joltage_2)
