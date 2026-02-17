'''Write a python program which reminds you of drinking water every hour or two.
 Your program can either beep or send desktop notifications for a specific operating system'''


import subprocess
import time

# subprocess.run([
#     "notify-send",
#     "Hello",
#     "This is a notification from Python!"
# ])


def reminder():
    start = time.time()
    while True:
        end = time.time()
        if end - start >= 3600 :
            subprocess.run([
                "notify-send",
                "Hello",
                "Reminder ---- Drink Water Now"
            ]) 
            start = time.time()


reminder()