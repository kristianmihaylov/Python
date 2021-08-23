import sys

text = input()
min = sys.maxsize

while text != "Stop":
    number = int(text)
    if number < min:
        min = number

    text = input()
print(min)