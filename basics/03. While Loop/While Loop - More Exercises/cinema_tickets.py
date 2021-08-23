import sys

enter = input()
student = 0
standard = 0
kid = 0
name = enter
saved_student = 0
saved_kid = 0
saved_standard = 0
film_percent = 0
saved_tickets = 0
slots = int(input())

for i in range(1, slots + 1):
    if enter != "Finish":
        enter = input()
        if enter == "student":
            student += 1
        elif enter == "kid":
            kid += 1
        elif enter == "standard":
            standard += 1
    else:
        film_percent = ((student + kid + standard) / slots) * 100
        saved_tickets += (student + kid + standard)
        saved_student += student
        saved_kid += kid
        saved_standard += standard
        print(f"{name} - {film_percent:.2f}% full.")
        student = 0
        kid = 0
        standard = 0
        break
    if enter == "End":
        enter = input()
        for i in range(1, slots + 1):
            if enter != "Finish":
                enter = input()
                if enter == "student":
                    student += 1
                elif enter == "kid":
                    kid += 1
                elif enter == "standard":
                    standard += 1
            else:
                film_percent = ((student + kid + standard) / slots) * 100
                saved_tickets += (student + kid + standard)
                saved_student += student
                saved_kid += kid
                saved_standard += standard
                print(f"{name} - {film_percent:.2f}% full.")
                student = 0
                kid = 0
                standard = 0
                break

print(f"Total tickets: {saved_tickets}")
print(f"{(saved_student / saved_tickets)*100:.2f}% student tickets")
print(f"{(saved_standard / saved_tickets)*100:.2f}% standard tickets")
print(f"{(saved_kid / saved_tickets)*100:.2f}% kids tickets")