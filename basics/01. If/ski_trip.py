days = int(input())
room = input()
rate = input()

# room_for_one_person = 18  per night
# apartment = 25 # per night
# president_apartment = 35 # per night

if days < 10:
    if room == "room for one person":
        price = (days - 1) * 18
    if room == "apartment":
        price = ((days - 1) * 25) * 0.7
    if room == "president apartment":
        price = ((days - 1) * 35) * 0.9
elif 10 <= days <= 15:
    if room == "room for one person":
        price = (days - 1) * 18
    if room == "apartment":
        price = ((days - 1) * 25) * 0.65
    if room == "president apartment":
        price = ((days - 1) * 35) * 0.85
elif days > 15:
    if room == "room for one person":
        price = (days - 1) * 18
    if room == "apartment":
        price = ((days - 1) * 25) * 0.5
    if room == "president apartment":
        price = ((days - 1) * 35) * 0.8

if rate == "positive":
    all_price = price + (price * 0.25)
elif rate == "negative":
    all_price = price * 0.9

print(f"{all_price:.2f}")