import time
from plyer import notification

while True:
    notification.notify(
        title = "💧 Water Reminder",
        message = "You need to drink Water, 1 Hour Completed",
        timeout = 5
    )
    # waiting time
    print("Reminder sent at", time.strftime("%I:%M:%S %p"))
    time.sleep(10)