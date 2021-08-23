n = int(input())
number = int(input())
sum = 0

sum += number

while n > sum:
    number = int(input())
    sum += number

print(sum)