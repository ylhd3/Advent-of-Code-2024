import os
import re

DIR = os.getcwd()

with open(DIR+"/inputs/Task_15_input.txt", 'r') as fd:
    map_text, directions = re.split("\n\n", fd.read())

print(map_text)
print(directions[0])

cols = 50
rows = 50

map_2d_array = [[None] * cols] * rows
y = 0
x = 0

print(map_2d_array)

for point_index in range(len(map_text)):
    if point_index % 51 == 0 and point_index != 0:
        y += 1
        x = 0

    match map_text[point_index]:
        case "#":
            map_2d_array[x][y] = "Wall"
        case "O":
            print(x, y)
            map_2d_array[x][y] = "Box"
            print(map_2d_array[x][y])
        case ".":
            map_2d_array[x][y] = None
        case "@":
            map_2d_array[x][y] = "Bot"

    x += 1

print(map_2d_array)
print(map_2d_array[49][49])
print(map_2d_array[1][1])
print(map_2d_array[2].index("Box"))
