n = int(input())
n1 = 0
n2 = 0
n3 = 0

p1 = 0
p2 = 0
p3 = 0

for i in range(1, n + 1):
    number = int(input())

    if number % 2 == 0:
        n1 += 1
        if number % 3 == 0:
            n2 += 1
            if number % 4 == 0:
                n3 += 1
        elif number % 4 == 0:
            n3 += 1


    elif number % 3 == 0:
        n2 += 1
        if number % 4 == 0:
            n3 += 1

    elif number % 4 == 0:
        n3 += 1

for i in range(1):
    p1 = (n1 / n) * 100
    print(f"{p1:.2f}%")

    p2 = (n2 / n) * 100
    print(f"{p2:.2f}%")

    p3 = (n3 / n) * 100
    print(f"{p3:.2f}%")
