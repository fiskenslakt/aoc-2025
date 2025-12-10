import re
from collections import deque
# from heapq import heappop, heappush

from aocd import data, submit

# data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """

# def cache(func):
#     D = {}
#     def inner(light_state, final_light_state, presses, buttons, last_pressed):
#         key = (light_state, final_light_state)
#         if key not in D:
#             D[key] = func(light_state, final_light_state, presses, buttons, last_pressed)
#         return D[key]
#     return inner


# @cache
# def dfs(light_state, final_light_state, presses, buttons, last_pressed):
#     if light_state == final_light_state:
#         return presses

#     press_options = []

#     for button in buttons:
#         button_mask = 0
#         for li in map(int, button_pattern.findall(button)):
#             button_mask += 2**li

#         if button_mask != last_pressed:
#             press_options.append(dfs(light_state ^ button_mask, final_light_state, presses + 1, buttons, button_mask))

#     return min(press_options)


button_pattern = re.compile(r"(\d+)")

machines = [line.split() for line in data.splitlines()]

fewest_presses = 0
# import pudb;pu.db
for machine in machines:
    lights, *buttons, joltages = machine
    final_light_state = int(lights[1:-1].replace(".", "0").replace("#", "1")[::-1], 2)

    # queue = deque([(0, 0, set())])
    queue = deque([(0, 0)])
    seen_states = set()
    # queue = [(final_light_state, 0, 0, set())]

    while queue:
        light_state, presses = queue.popleft()
        # final_state_diff, presses, light_state, seen_states = heappop(queue)

        if light_state == final_light_state:
            fewest_presses += presses
            break

        for button in buttons:
            button_mask = 0
            for li in map(int, button_pattern.findall(button)):
                button_mask += 2**li

            new_light_state = light_state ^ button_mask

            if new_light_state not in seen_states:
                # queue.append((new_light_state, presses + 1, seen_states | {new_light_state}))
                queue.append((new_light_state, presses + 1))
                seen_states.add(new_light_state)
                # heappush(queue, (abs(final_light_state - new_light_state), presses + 1, new_light_state, seen_states | {new_light_state}))

submit(fewest_presses)
