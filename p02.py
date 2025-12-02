from itertools import batched

from aocd import data, submit

# data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""

id_ranges = data.split(",")

id_sum = 0
# import pudb;pu.db
# for id_range in id_ranges:
#     x, y = id_range.split("-")
#     for _id in range(int(x), int(y)+1):
#         _id = str(_id)
#         if _id[:len(_id)//2] == _id[len(_id)//2:]:
#             # print(_id)
#             id_sum += int(_id)
    # print()

# submit(id_sum)

for id_range in id_ranges:
    x, y = id_range.split("-")
    for _id in range(int(x), int(y)+1):
        s_id = str(_id)
        for chunk_size in range(1, len(s_id)):
            if len(s_id) % chunk_size != 0:
                continue
            chunks = list(batched(s_id, chunk_size))
            for chunk in chunks[1:]:
                if chunk != chunks[0]:
                    break
            else:
                id_sum += _id
                break

submit(id_sum)
