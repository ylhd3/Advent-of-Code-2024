import os
import re

DIR = os.getcwd()

with open(DIR+"/inputs/Task_13_input.txt", 'r') as fd:
    full_text = re.split("\n\n", fd.read())

claw_dict = {}
A_X_regex = r"(?<=A: X\+)\d*"
A_Y_regex = r"(?<=Y\+)\d*(?=\nButton B)"
B_X_regex = r"(?<=B: X\+)\d*"
B_Y_regex = r"(?<=Y\+)\d*(?=\nPrize)"
Prize_X_regex = r"(?<=Prize: X\=)\d*"
Prize_Y_regex = r"(?<=Y\=)\d*$"

fewest_tokens = 0

for block_no in range(len(full_text)):
    A = tuple(map(int, (re.search(A_X_regex, full_text[block_no])[0], re.search(A_Y_regex, full_text[block_no])[0])))
    B = tuple(map(int, (re.search(B_X_regex, full_text[block_no])[0], re.search(B_Y_regex, full_text[block_no])[0])))
    Prize = tuple(map(int, (re.search(Prize_X_regex, full_text[block_no])[0], re.search(Prize_Y_regex, full_text[block_no])[0])))

    B_amount = ((Prize[1]*A[0]) - (Prize[0]*A[1])) / ((B[1]*A[0]) - (B[0]*A[1]))
    A_amount = ((Prize[1]*B[0]) - (Prize[0]*B[1])) / ((A[1]*B[0]) - (A[0]*B[1]))

    if B_amount.is_integer() and A_amount.is_integer() and A_amount >= 0 and B_amount >= 0:
        print("A: " + str(A_amount) + " | B: " + str(B_amount) + " for prize " + str(Prize[0]) + ", " + str(Prize[1]))
        fewest_tokens = fewest_tokens + (A_amount * 3)
        fewest_tokens = fewest_tokens + (B_amount * 1)

print("Fewest tokens needed for prizes are " + str(fewest_tokens))

fewest_tokens = 0

for block_no in range(len(full_text)):
    A = tuple(map(int, (re.search(A_X_regex, full_text[block_no])[0], re.search(A_Y_regex, full_text[block_no])[0])))
    B = tuple(map(int, (re.search(B_X_regex, full_text[block_no])[0], re.search(B_Y_regex, full_text[block_no])[0])))
    Prize = list(map(int, (re.search(Prize_X_regex, full_text[block_no])[0], re.search(Prize_Y_regex, full_text[block_no])[0])))
    Prize[0] += 10000000000000
    Prize[1] += 10000000000000

    B_amount = ((Prize[1]*A[0]) - (Prize[0]*A[1])) / ((B[1]*A[0]) - (B[0]*A[1]))
    A_amount = ((Prize[1]*B[0]) - (Prize[0]*B[1])) / ((A[1]*B[0]) - (A[0]*B[1]))

    if B_amount.is_integer() and A_amount.is_integer() and A_amount >= 0 and B_amount >= 0:
        print("A: " + str(A_amount) + " | B: " + str(B_amount) + " for prize " + str(Prize[0]) + ", " + str(Prize[1]))
        fewest_tokens = fewest_tokens + (A_amount * 3)
        fewest_tokens = fewest_tokens + (B_amount * 1)

print("Fewest tokens needed for prizes with the 10000000000000 increase are " + str(fewest_tokens))






