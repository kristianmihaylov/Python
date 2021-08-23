import sys

start = int(input())
stop = int(input())
magic_number = int(input())
combination = 0
is_found = False

for first_number in range(start, stop + 1):
    for second_number in range(start, stop + 1):
        combination += 1
        if first_number + second_number == magic_number:
            is_found = True
            print(f"Combination N:{combination} ({first_number} + {second_number} = {magic_number})")
            sys.exit()


if not is_found:
    print(f"{combination} combinations - neither equals {magic_number}")