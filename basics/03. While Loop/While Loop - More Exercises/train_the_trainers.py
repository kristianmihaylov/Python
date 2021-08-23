number_jury = int(input())
command = input()
final_grade = 0
number_presentations = 0
avarage_presentation_grade = 0
while command != "Finish":
    current_presentation_name = command
    number_presentations += 1
    current_presentation_grade = 0
    for presentation_grade in range(number_jury):
        current_grade = float(input())
        avarage_presentation_grade += current_grade
    avarage_presentation_grade /= number_jury
    final_grade += avarage_presentation_grade
    print(f"{current_presentation_name} - {avarage_presentation_grade:.2f}.")
    command = input()
final_avarage_grade = final_grade / number_presentations
print(f"Student's final assessment is {final_avarage_grade:.2f}.")