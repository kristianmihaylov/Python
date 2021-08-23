n = int(input())
com = 0

for n1 in range(0, n + 1):
    for n2 in range(0, n + 1):
        for n3 in range(0, n + 1):
            i = n1 + n2 + n3
            if i == n:
                com += 1

print(com)