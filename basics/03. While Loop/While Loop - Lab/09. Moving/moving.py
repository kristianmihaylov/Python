width_area = int(input())
length_area = int(input())
height_area = int(input())

command = input()
area = 0
solution = 0

while command != "Done":
    area = width_area * length_area * height_area
    number = int(command)
    solution += number
    if solution >= area:
        print(f"No more free space! You need {solution - area} Cubic meters more.")
        break
    else:
        command = input()
if area == solution or command == "Done":
    print(f"{area - solution} Cubic meters left.")