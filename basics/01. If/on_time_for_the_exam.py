hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

time_exam = hour_exam * 60 + minute_exam
time_arrive = hour_arrive * 60 + minute_arrive

if time_arrive == time_exam:
    print("On time")
elif 0 > time_arrive >= (time_exam - 30):
    print("On time")
    print(f"{time_exam - time_arrive} minutes before the start")
elif (time_exam - 59) < time_arrive < (time_exam - 30):
    print("Early")
    print(f"{time_exam - time_arrive} minutes before the start")
elif time_arrive <= (time_exam - 60) and 0 < minute_arrive <= 9:
    print("Early")
    print(f"{hour_exam - hour_arrive}:0{minute_exam - minute_arrive} hours before the start")
elif time_arrive <= (time_exam - 60) and minute_arrive >= 10:
    print("Early")
    print(f"{hour_exam - hour_arrive}:{minute_exam - minute_arrive} hours before the start")
elif time_arrive > (time_exam) and 0 < minute_arrive <= 9:
    print("Late")
    print(f"{hour_arrive - hour_exam}:0{minute_arrive - minute_exam} hours before the start")
elif time_arrive > (time_exam) and minute_arrive >= 10:
    print("Late")
    print(f"{hour_arrive - hour_exam}:{minute_arrive - minute_exam} hours before the start")
elif time_arrive > (time_exam):
    print("Late")
    print(f"{time_arrive - time}hours before the start")