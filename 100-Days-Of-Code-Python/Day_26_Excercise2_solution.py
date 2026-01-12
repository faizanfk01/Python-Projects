import time

current_time = time.localtime()

current_hour = time.strftime("%H", current_time)

if int(current_hour) < 12:
    print("Good Morning Sir!")

elif 12 <= int(current_hour) < 18:
    print("Good Afternoon sir!")
    
else:
    print("Good Night sir!")