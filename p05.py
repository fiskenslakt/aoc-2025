from aocd import data


def overlap(r1: range, r2: range):
    return r1.stop > r2.start and r2.stop > r1.start


raw_id_ranges, available_ids = data.split("\n\n")

fresh_id_ranges = []

for id_range in raw_id_ranges.splitlines():
    lower, upper = map(int, id_range.split("-"))
    fresh_id_ranges.append(range(lower, upper + 1))

fresh = 0

for available_id in available_ids.splitlines():
    for id_range in fresh_id_ranges:
        if int(available_id) in id_range:
            fresh += 1
            break

fresh_id_ranges.sort(key=lambda r: r.start)
unique_ranges = []

cur_range = fresh_id_ranges[0]
for next_range in fresh_id_ranges[1:]:
    if overlap(cur_range, next_range):
        cur_range = range(
            min(cur_range.start, next_range.start), max(cur_range.stop, next_range.stop)
        )
    else:
        unique_ranges.append(cur_range)
        cur_range = next_range

unique_ranges.append(cur_range)

print("Part 1:", fresh)
print("Part 2:", sum(map(len, unique_ranges)))
