from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

# Reminder interval (in seconds)
# 3600 = 1 hour, 7200 = 2 hours
interval = 3600     # change to 7200 if you want a 2-hour reminder

while True:
    toaster.show_toast(
        "💧 Water Reminder",
        "Time to drink water!",
         
        duration=10,       # notification stays for 10 seconds
        threaded=True
    )

    # Wait (sleep) for the next reminder
    time.sleep(interval)