hours = int(input())
minutes = int(input())

if hours <= 23:
    h = hours
elif hours == 0:
    h = hours * 0
elif hours == 24:
    h = hours * 0
elif hours > 24:
    h = hours - 24

if minutes <= 59:
    m = minutes
elif minutes == 0:
    m = minutes * 0
elif minutes == 60:
    m = minutes * 0
elif minutes > 60:
    m = minutes - 60

sloved_m = m + 15

if sloved_m <= 59:
    m = sloved_m
elif sloved_m == 60:
    m = sloved_m * 0
    h = hours + 1
elif sloved_m > 60:
    m = sloved_m - 60
    h = hours + 1

if h == 24:
    h = hours * 0
elif h > 24:
    h = hours - 24

if m < 10:
    print(f"{h}:0{m}")
else:
    print(f"{h}:{m}")
