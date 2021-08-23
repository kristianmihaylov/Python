town = input()
sell = float(input())

if town == "Sofia":
    if 0 > sell:
        print("error")
    if 0 <= sell <= 500:
        commission = sell * 0.05
        print(f"{commission:.2f}")
    elif 500.00 < sell <= 1000.00:
        commission = 0.07 * sell
        print(f"{commission:.2f}")
    elif 1000.00 < sell <= 10000.00:
        commission = 0.08 * sell
        print(f"{commission:.2f}")
    elif sell > 10000:
        commission = 0.12 * sell
        print(f"{commission:.2f}")
elif town == "Varna":
    if 0 > sell:
        print("error")
    if 0.00 <= sell <= 500.00:
        commission = sell * 0.045
        print(f"{commission:.2f}")
    elif 500.00 < sell <= 1000.00:
        commission = 0.075 * sell
        print(f"{commission:.2f}")
    elif 1000.00 < sell <= 10000.00:
        commission = 0.1 * sell
        print(f"{commission:.2f}")
    elif sell > 10000:
        commission = 0.13 * sell
        print(f"{commission:.2f}")
elif town == "Plovdiv":
    if 0 > sell:
        print("error")
    if 0.00 <= sell <= 500.00:
        commission = sell * 0.055
        print(f"{commission:.2f}")
    elif 500.00 < sell <= 1000.00:
        commission = 0.08 * sell
        print(f"{commission:.2f}")
    elif 1000.00 < sell <= 10000.00:
        commission = 0.12 * sell
        print(f"{commission:.2f}")
    elif sell > 10000:
        commission = 0.145 * sell
        print(f"{commission:.2f}")
else:
    print("error")