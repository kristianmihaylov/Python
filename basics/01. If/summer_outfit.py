degrees = int(input())
time_of_day = input()

if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif time_of_day == "Afternoon":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif time_of_day == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif 18 < degrees <= 24:
    if time_of_day == "Morning":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif time_of_day == "Afternoon":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif time_of_day == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
elif degrees >= 25:
    if time_of_day == "Morning":
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif time_of_day == "Afternoon":
        print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")
    elif time_of_day == "Evening":
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")