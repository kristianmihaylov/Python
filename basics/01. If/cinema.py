type_of_the_movie = input()
rows = int(input())
colums = int(input())

total_places = rows * colums
price_of_the_ticket = 0

if type_of_the_movie == "Premiere":
    price_of_the_ticket = 12
elif type_of_the_movie == "Normal":
    price_of_the_ticket = 7.5
else:
    price_of_the_ticket = 5

total_income = total_places * price_of_the_ticket
print(f"{total_income:.2f} leva")