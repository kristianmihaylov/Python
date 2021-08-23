n = int(input())

for current_number in range(1111, 9999 + 1):
    is_special = True
    current_number_str = str(current_number)
    for current_digit in current_number_str:
        if int(current_digit) == 0 or n % int(current_digit) != 0:
            is_special = False
            break
    if is_special:
        print(current_number, end=" ")