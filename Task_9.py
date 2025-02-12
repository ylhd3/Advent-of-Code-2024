import os
import re
import datetime

DIR = os.getcwd()
file_id = 0
expanded_map_list = []

with open(DIR+"/inputs/Task_9_input.txt", 'r') as fd:
    disk_map = re.sub("\n", "", fd.read())

is_file = True

# test_string = "00992111777.44.333....5555.6666.....8888.."
# test_map = []
# for c in test_string:
#     if c != ".":
#         test_map.append(c)
#     else:
#         test_map.append(None)
#
# test_checksum = 0
#
# for test_item_index in range(len(test_map)):
#     if test_map[test_item_index] is not None:
#         test_checksum = test_checksum + (test_item_index * int(test_map[test_item_index]))
#
# print("Test checksum: " + str(test_checksum))

for digit in disk_map:
    if is_file:
        for i in range(int(digit)):
            expanded_map_list.append(file_id)

        file_id += 1
        is_file = not is_file

    else:  # Free space
        for i in range(int(digit)):
            expanded_map_list.append(None)

        is_file = not is_file

print("Disk map expanded")

print("----Part 1----")
last_file = 0
leftmost_none_index = 0

fragmented_map_list = expanded_map_list.copy()

while None in fragmented_map_list:
    last_file = fragmented_map_list.pop()
    if last_file is not None:
        leftmost_none_index = fragmented_map_list.index(None)
        fragmented_map_list[leftmost_none_index] = last_file

# print(fragmented_map_list)
print("File blocks moved")
checksum = 0

for block_position in range(len(fragmented_map_list)):
    checksum = checksum + (block_position * fragmented_map_list[block_position])

print("Filesystem's checksum: " + str(checksum))

print(expanded_map_list[:100])
print(expanded_map_list[len(expanded_map_list) - 100:])

print("----Part 2----")

no_files = file_id
print(str(no_files - 1) + " files to check and potentially move | " + str(datetime.datetime.now().time()))

for i in reversed(range(1, no_files)):
    can_move = False
    file_count = expanded_map_list.count(i)
    leftmost_initial_none_index = expanded_map_list.index(None)
    file_initial_index = expanded_map_list.index(i)
    while not can_move:
        none_count = 0
        leftmost_none_index = leftmost_initial_none_index
        if leftmost_initial_none_index > expanded_map_list.index(i):
            break

        while expanded_map_list[leftmost_none_index] is None:
            if leftmost_none_index == len(expanded_map_list) - 1:
                break
            none_count += 1
            leftmost_none_index += 1

        if file_count <= none_count:
            expanded_map_list[file_initial_index:file_initial_index + file_count] = [None] * file_count
            expanded_map_list[leftmost_initial_none_index:leftmost_initial_none_index + file_count] = [i] * file_count
            can_move = True
        else:
            # print("Adjacent file: " + str(expanded_map_list[leftmost_none_index+1]) + " | Current leftmost None index: " + str(leftmost_none_index) + " | Checking next Nones")
            leftmost_initial_none_index = expanded_map_list[leftmost_none_index+1:].index(None) + leftmost_none_index + 1
            # print("New leftmost none index: " + str(leftmost_initial_none_index))

        if leftmost_initial_none_index == len(expanded_map_list) - 1:
            break

    # print(expanded_map_list[:100])
    # print(str(i - 1) + " files to check and potentially move")
    if (i % 500) == 0:
        print(str(i) + " files to check and potentially move | " + str(datetime.datetime.now().time()))

print(expanded_map_list[:100])
print(expanded_map_list[len(expanded_map_list) - 100:])

print("File blocks moved")
checksum = 0

for block_position in range(len(expanded_map_list)):
    if expanded_map_list[block_position] is not None:
        checksum = checksum + (block_position * expanded_map_list[block_position])

print("Filesystem's checksum: " + str(checksum))
