flower_type = input()
flower_amount = int(input())
budget = int(input())

if flower_type == "Roses":
    if flower_amount > 80:
        price = (5 * flower_amount) * 0.9
    else:
        price = 5 * flower_amount
elif flower_type == "Dahlias":
    if flower_amount > 90:
        price = (3.80 * flower_amount) * 0.85
    else:
        price = 3.80 * flower_amount
elif flower_type == "Tulips":
    if flower_amount > 80:
        price = (2.80 * flower_amount) * 0.85
    else:
        price = 2.80 * flower_amount
elif flower_type == "Narcissus":
    if 0 <= flower_amount < 120:
        price = ((3 * flower_amount) * 0.15) + ( 3 * flower_amount)
    else:
        price = 3 * flower_amount
elif flower_type == "Gladiolus":
    if 0 <= flower_amount < 80:
        price = ((2.50 * flower_amount) * 0.20) + (2.50 * flower_amount)
    else:
        price = 2.50 * flower_amount

if price <= budget:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")