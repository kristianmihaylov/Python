name = input()
rating = float(input())
last_rating = 0
grade = 1

while rating >= 4:
    grade += 1
    last_rating += rating
    if grade == 12:
        print(f"{name} graduated. Average grade: {last_rating / 12:.2f}")
        break
    else:
        rating = float(input())
else:
    print(f"{name} has been excluded at {grade} grade")