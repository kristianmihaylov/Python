import sys
n = int(input())
odd_max = - sys.maxsize
odd_min = + sys.maxsize
odd_sum = 0
even_max = - sys.maxsize
even_min = + sys.maxsize
even_sum = 0

for i in range(1, n + 1, 2):
    number = float(input())
    odd_sum += number
    if number > odd_max:
        odd_max = number
    if number < odd_min:
        odd_min = number

for i in range(1, n + 1, 2):
    number = float(input())
    even_sum += number
    if number > even_max:
        even_max = number
    if number < even_min:
        even_min = number

if n == 0:
    print("OddSum=0.00,")
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No,")
elif n != 0:
    print(f"OddSum={odd_sum:.2f},")
    if odd_min == 0:
        print(f"OddMin=No,")
    else:
        print(f"OddMin={odd_min:.2f},")
    if odd_max == 0:
        print(f"OddMax=No,")
    else:
        print(f"OddMax={odd_max:.2f},")

    print(f"EvenSum={even_sum:.2f},")
    if even_min == 0:
        print(f"EvenMin=No,")
    else:
        print(f"EvenMin={even_min:.2f},")
    if even_max == 0:
        print(f"EvenMax=No,")
    else:
        print(f"EvenMax={even_max:.2f},")