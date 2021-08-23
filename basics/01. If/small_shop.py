product = input()
city = input()
amount = float(input())

if city == "Sofia":
    if product == "coffee":
        slove = 0.50 * amount
    elif product == "water":
        slove = 0.80 * amount
    elif product == "beer":
        slove = 1.20 * amount
    elif product == "sweets":
        slove = 1.45 * amount
    elif product == "peanuts":
        slove = 1.60 * amount
elif city == "Plovdiv":
    if product == "coffee":
        slove = 0.40 * amount
    elif product == "water":
        slove = 0.70 * amount
    elif product == "beer":
        slove = 1.15 * amount
    elif product == "sweets":
        slove = 1.30 * amount
    elif product == "peanuts":
        slove = 1.50 * amount
elif city == "Varna":
    if product == "coffee":
        slove = 0.45 * amount
    elif product == "water":
        slove = 0.70 * amount
    elif product == "beer":
        slove = 1.10 * amount
    elif product == "sweets":
        slove = 1.35 * amount
    elif product == "peanuts":
        slove = 1.55 * amount

print(slove)