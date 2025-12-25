import re
from collections import deque
from functools import cache
from itertools import chain, combinations

from aocd import data, submit

# data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """


def powerset(iterable):
    return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable) + 1))


@cache
def dfs(joltages, buttons):
    if not any(joltages):
        return 0

    joltage_parity = int("".join(str(j % 2) for j in joltages)[::-1], 2)
    min_presses = float("inf")

    for button_combo in powerset(buttons):
        button_parity = 0
        reductions = [0] * len(joltages)

        for button in button_combo:
            button_mask = 0
            for b_idx in button_pattern.findall(button):
                button_mask += 2 ** int(b_idx)
                reductions[int(b_idx)] += 1

            button_parity ^= button_mask

        if button_parity == joltage_parity:
            new_joltages = []

            possible = True
            for j, r in zip(joltages, reductions):
                diff = j - r
                if diff < 0:
                    possible = False
                    break
                new_joltages.append(diff // 2)

            if not possible:
                continue

            presses = len(button_combo) + 2 * dfs(tuple(new_joltages), buttons)
            min_presses = min(min_presses, presses)

    return min_presses


button_pattern = re.compile(r"(\d+)")

machines = [line.split() for line in data.splitlines()]

light_indicator_fewest_presses = 0
joltages_fewest_presses = 0
# import pudb;pu.db
# print("total machines:", len(machines))
for mi, machine in enumerate(machines):
    # print(mi, machine)
    lights, *buttons, joltages = machine
    final_light_state = int(lights[1:-1].replace(".", "0").replace("#", "1")[::-1], 2)

    queue = deque([(0, 0)])
    seen_states = set()

    # while queue:
    #     light_state, presses = queue.popleft()

    #     if light_state == final_light_state:
    #         light_indicator_fewest_presses += presses
    #         break

    #     for button in buttons:
    #         button_mask = 0
    #         for li in map(int, button_pattern.findall(button)):
    #             button_mask += 2**li

    #         new_light_state = light_state ^ button_mask

    #         if new_light_state not in seen_states:
    #             queue.append((new_light_state, presses + 1))
    #             seen_states.add(new_light_state)

    final_joltages = tuple(map(int, button_pattern.findall(joltages)))

    print(dfs(final_joltages, tuple(buttons)))
    joltages_fewest_presses += dfs(final_joltages, tuple(buttons))
    dfs.cache_clear()


# print("Part 1:", light_indicator_fewest_presses)
print(joltages_fewest_presses)
