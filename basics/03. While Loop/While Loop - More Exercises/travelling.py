place = input()

while place != "End":
    price = float(input())
    money = 0
    while money < price:
        saved_money = float(input())
        money += saved_money
    else:
        print(f"Going to {place}!")

    place = input()