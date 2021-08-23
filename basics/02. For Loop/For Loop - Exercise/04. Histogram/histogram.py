n = int(input())
number = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, n):
    number = int(input())
    if number < 200:
        number1 += 1
    elif number <= 399:
        number2 += 1
    elif number <= 599:
        number3 += 1
    elif number <= 799:
        number4 += 1
    elif 800 <= number <= 1000:
        number5 += 1

for i in range(1):
    p1 = (number1 / n) * 100
    print(f"{p1:.2f}%")

    p2 = (number2 / n) * 100
    print(f"{p2:.2f}%")

    p3 = (number3 / n) * 100
    print(f"{p3:.2f}%")

    p4 = (number4 / n) * 100
    print(f"{p4:.2f}%")

    p5 = (number5 / n) * 100
    print(f"{p5:.2f}%")

