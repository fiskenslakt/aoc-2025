from itertools import batched

from aocd import data

id_ranges = data.split(",")

invalid_id_sum_1 = 0
invalid_id_sum_2 = 0

for id_range in id_ranges:
    min_range, max_range = map(int, id_range.split("-"))
    for product_id in range(min_range, max_range + 1):
        product_id_str = str(product_id)
        i = len(product_id_str) // 2

        if product_id_str[:i] == product_id_str[i:]:
            invalid_id_sum_1 += product_id

        for chunk_size in range(1, len(product_id_str)):
            if len(product_id_str) % chunk_size != 0:
                continue
            chunks = list(batched(product_id_str, chunk_size))
            for chunk in chunks[1:]:
                if chunk != chunks[0]:
                    break
            else:
                invalid_id_sum_2 += product_id
                break

print("Part 1:", invalid_id_sum_1)
print("Part 2:", invalid_id_sum_2)
