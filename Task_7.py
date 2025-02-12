import itertools

import numpy as np
import os
import re
import math

DIR = os.getcwd()
input_dict = {}

with open(DIR+"/inputs/Task_7_input.txt", 'r') as fd:
    for line in fd:
        result, numbers_line = re.split(":", line)
        input_dict[int(result)] = list(map(int, re.split(" |\n", numbers_line)[1:-1]))


def calculate(pred_result, numbers_list, no_ops):
    all_ops_list = list(itertools.product("*+", repeat=no_ops))
    solvable_list = []

    # print(numbers_list)
    # print(str(all_ops_list))

    for ops_list in all_ops_list:
        actual_result = numbers_list[0]
        for i in range(1, len(numbers_list)):
            match ops_list[i-1]:
                case "*":
                    actual_result = actual_result * numbers_list[i]
                case "+":
                    actual_result = actual_result + numbers_list[i]

        if actual_result == pred_result:
            solvable_list.append(True)
        else:
            solvable_list.append(False)

    return solvable_list

print(input_dict)

solvable_result_list = []
solvable_sum = 0

for cal_result in input_dict:
    no_ops = len(input_dict[cal_result]) - 1
    solvable_result_list = calculate(cal_result, input_dict[cal_result], no_ops)

    if True in solvable_result_list:
        solvable_sum += cal_result

print("Total calibration result: " + str(solvable_sum))


def new_calculate(pred_result, numbers_list, no_ops):
    all_ops_list = itertools.product("*+|", repeat=no_ops)
    solvable_list = []

    # print(numbers_list)
    # print(str(all_ops_list))

    for ops_list in all_ops_list:
        actual_result = numbers_list[0]
        for i in range(1, len(numbers_list)):
            match ops_list[i-1]:
                case "*":
                    actual_result = actual_result * numbers_list[i]
                case "+":
                    actual_result = actual_result + numbers_list[i]
                case "|":
                    actual_result = int(str(actual_result) + str(numbers_list[i]))

        if actual_result == pred_result:
            solvable_list.append(True)
        else:
            solvable_list.append(False)

    return solvable_list

solvable_result_list = []
solvable_sum = 0

for cal_result in input_dict:
    no_ops = len(input_dict[cal_result]) - 1
    solvable_result_list = new_calculate(cal_result, input_dict[cal_result], no_ops)

    if True in solvable_result_list:
        solvable_sum += cal_result

print("New total calibration result: " + str(solvable_sum))
