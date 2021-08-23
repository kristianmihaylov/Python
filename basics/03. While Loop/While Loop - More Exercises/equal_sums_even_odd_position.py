first_number = int(input())
last_number = int(input())

for current_number in range(first_number, last_number + 1):
    odd_sum = 0
    even_sum = 0
    current_number_str = str(current_number)
    for index, digit in enumerate(current_number_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(current_number, end=" ")