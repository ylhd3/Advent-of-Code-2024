import os
import re
import datetime

import numpy as np

DIR = os.getcwd()

with open(DIR+"/inputs/Task_11_input.txt", 'r') as fd:
    initial_stone_list = re.split(" ", re.sub("\n", "", fd.read()))

print("At no blinks, the " + str(len(initial_stone_list)) + " stones are " + str(initial_stone_list))

stone_list = initial_stone_list.copy()

# In 25 blinks
for blink_no in range(25):
    next_stone_list = []
    for stone_no in range(len(stone_list)):
        if stone_list[stone_no] == "0":  # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            next_stone_list.append("1")
        elif (len(stone_list[stone_no]) % 2) == 0: # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            stone_engrave_len = len(stone_list[stone_no])
            stone_pair = [stone_list[stone_no][:stone_engrave_len // 2], stone_list[stone_no][stone_engrave_len // 2:]]
            for pair_no in range(len(stone_pair)):
                pair = stone_pair[pair_no]
                leading_zeros = True
                while leading_zeros:
                    try:
                        if pair.index("0") == 0:
                            if len(pair) == 1:
                                leading_zeros = False
                            else:
                                pair = pair[1:]

                        else:
                            leading_zeros = False
                    except ValueError as ve:
                        leading_zeros = False

                stone_pair[pair_no] = pair

            next_stone_list += stone_pair

        else: # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            next_stone_list.append(str(int(stone_list[stone_no]) * 2024))

    print("At " + str(blink_no + 1) + " blink(s), there are " + str(len(next_stone_list)) + " stones")
    if len(next_stone_list) < 30:
        print(next_stone_list)
    stone_list = next_stone_list.copy()

stones_dict_odd = {}
stones_dict_even = {}

for stone in initial_stone_list:
    if int(stone) in stones_dict_odd.keys():
        stones_dict_odd[int(stone)] += 1
    else:
        stones_dict_odd[int(stone)] = 1

print(stones_dict_odd)

for blink_no in range(1, 76):
    if (blink_no % 2) == 0:
        curr_stones_dict = stones_dict_even
        stones_dict_odd = {}
        next_stone_list = stones_dict_odd
    else:
        curr_stones_dict = stones_dict_odd
        stones_dict_even = {}
        next_stone_list = stones_dict_even

    for stone in curr_stones_dict.keys():
        if stone != 0:
            stone_len = np.floor(np.log10(stone)) + 1  # log of any number will give the number of digits - 1 | log 10 = 1, log 100 = 2
        else:
            stone_len = 1

        if stone == 0:
            if 1 in next_stone_list.keys():
                next_stone_list[1] += curr_stones_dict[stone]
            else:
                next_stone_list[1] = curr_stones_dict[stone]
        elif (stone_len % 2) == 0:
            temp_pair = map(int, divmod(stone, 10**(stone_len/2)))
            for pair in temp_pair:
                if pair in next_stone_list.keys():
                    next_stone_list[pair] += curr_stones_dict[stone]
                else:
                    next_stone_list[pair] = curr_stones_dict[stone]
        else:
            new_stone = stone * 2024
            if new_stone in next_stone_list.keys():
                next_stone_list[new_stone] += curr_stones_dict[stone]
            else:
                next_stone_list[new_stone] = curr_stones_dict[stone]

    print("At " + str(blink_no) + " blink(s), there are " + str(sum(next_stone_list.values())) + " stones")
    if blink_no < 8:
        print(next_stone_list)

    if blink_no == 25:
        print(next_stone_list)

# for stone in initial_stone_list:
#     if stone == "0":
#         stones_dict_dict["0"][key_0] = stone
#         key_0 += 1
#     elif len(stone) % 2 == 0:
#         stones_dict_dict["even"][key_even] = stone
#         key_even += 1
#     else:
#         stones_dict_dict["else"][key_else] = stone
#         key_else += 1
#
# print(stones_dict_dict)
#
# # In 75 blinks
# for blink_no in range(75):
#     next_stone_dict_dict = {}
#     key_0 = 0
#     key_even = 0
#     key_else = 0
#     next_stone_dict_dict["0"] = {}
#     next_stone_dict_dict["even"] = {}
#     next_stone_dict_dict["else"] = {}
#
#     for stone_key in stones_dict_dict["0"]:
#         stone = stones_dict_dict["0"][stone_key]
#         next_stone_dict_dict["else"][key_else] = "1"
#         key_else += 1
#
#     for stone_key in stones_dict_dict["even"]:
#         stone = stones_dict_dict["even"][stone_key]
#         stone_len = len(stone)
#         temp_pair = map(str, map(int, (stone[:stone_len//2], stone[stone_len//2:])))
#         for pair in temp_pair:
#             if pair == "0":
#                 next_stone_dict_dict["0"][key_0] = pair
#                 key_0 += 1
#             elif len(pair) % 2 == 0:
#                 next_stone_dict_dict["even"][key_even] = pair
#                 key_even += 1
#             else:
#                 next_stone_dict_dict["else"][key_else] = pair
#                 key_else += 1
#
#     for stone_key in stones_dict_dict["else"]:
#         stone = stones_dict_dict["else"][stone_key]
#         temp_stone = str(int(stone) * 2024)
#         if len(temp_stone) % 2 == 0:
#             next_stone_dict_dict["even"][key_even] = temp_stone
#             key_even += 1
#         else:
#             next_stone_dict_dict["else"][key_else] = temp_stone
#             key_else += 1
#
    # print("At " + str(blink_no + 1) + " blink(s), there are " + str(len(next_stone_dict_dict["0"]) +
    #                                                                 len(next_stone_dict_dict["even"]) +
    #                                                                 len(next_stone_dict_dict["else"])) + " stones")
#     # if len(next_stone_dict_dict) < 30:
#     #     print(next_stone_dict_dict)
#     stones_dict_dict = next_stone_dict_dict.copy()




