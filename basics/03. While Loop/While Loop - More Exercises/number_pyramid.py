final_number = int(input())
counter = 1
all_is_printed = False

for row in range(1, final_number + 1):
    for column in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > final_number:
            all_is_printed = True
            break
    if all_is_printed:
        break
    print()