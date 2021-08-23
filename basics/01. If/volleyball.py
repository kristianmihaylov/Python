import math

year = input()
holidays = int(input())
weekends_in_home_town = int(input())

weekends_per_year = 48

weekends_in_sofia = weekends_per_year - weekends_in_home_town
games_sofia = weekends_in_sofia * 3/4
games_sofia_in_holidays = holidays * 2/3

all_games_sofia = games_sofia + games_sofia_in_holidays + weekends_in_home_town

if year == "leap":
    leap_all_games_sofia = 0.15 * all_games_sofia
    slove = leap_all_games_sofia + all_games_sofia
    print(math.floor(slove))
elif year == "normal":
    slove = all_games_sofia
    print(math.floor(slove))