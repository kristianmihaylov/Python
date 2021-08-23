n = int(input()) # in 1 to 10
salary = int(input())


still_have_salary = True
for space in range(n):
    site = input()
    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50
    else:
        salary += 0

    if salary <= 0:
        still_have_salary = False
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
