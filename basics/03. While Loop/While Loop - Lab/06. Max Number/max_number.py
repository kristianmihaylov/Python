import sys
max = - sys.maxsize
text = input()
while text != "Stop":
    number = int(text)
    if number > max:
        max = number

    text = input()
print(max)