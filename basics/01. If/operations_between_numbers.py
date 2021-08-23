number1 = int(input())
number2 = int(input())
symbol = input()

solution = 0

if symbol == "+":
    solution = number1 + number2
    if solution % 2 == 0:
        print(f"{number1} + {number2} = {solution} - even")
    elif solution == 0:
        print(f"{number1} + {number2} = {solution}")
    else:
        print(f"{number1} + {number2} = {solution} - odd")
elif symbol == "-":
    solution = number1 - number2
    if solution % 2 == 0:
        print(f"{number1} - {number2} = {solution} - even")
    elif solution == 0:
        print(f"{number1} - {number2} = {solution}")
    else:
        print(f"{number1} - {number2} = {solution} - odd")
elif symbol == "*":
    solution = number1 * number2
    if solution % 2 == 0:
        print(f"{number1} * {number2} = {solution} - even")
    elif solution == 0:
        print(f"{number1} * {number2} = {solution}")
    else:
        print(f"{number1} * {number2} = {solution} - odd")
elif symbol == "/" and number2 != 0:
    solution = number1 / number2
    if solution % 2 == 0:
        print(f"{number1} / {number2} = {solution} - even")
    elif solution == 0:
        print(f"{number1} / {number2} = {solution}")
    else:
        print(f"{number1} / {number2} = {solution} - odd")
elif symbol == "/" and number2 == 0:
    print(f"Cannot divide {number1} by zero")
elif symbol == "%" and number2 != 0:
    slove = number1 % number2
    print(f"{number1} % {number2} = {slove}")
else:
    print(f"Cannot divide {number1} by zero")