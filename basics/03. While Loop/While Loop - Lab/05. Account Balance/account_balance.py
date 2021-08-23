money = input()
sum_money = 0
value = 0

while money != "NoMoreMoney":
    value = float(money)
    if value > 0:
        sum_money += value
        print(f"Increase: {value:.2f}")
    elif value <= 0:
        print("Invalid operation!")
        break

    money = input()

print(f"Total: {sum_money}")