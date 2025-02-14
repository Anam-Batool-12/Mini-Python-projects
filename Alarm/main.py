from playsound import playsound
import time

seconds = 10  # Set the duration in seconds
time_elapsed = 0
print("Alarm will start in 10 seconds")
while time_elapsed < seconds:
    time.sleep(1)
    time_elapsed += 1
    time_left = seconds - time_elapsed
    minutes, sec = divmod(time_left, 60)
    print(f"Time left: {minutes} minutes, {sec} seconds")
print("Alarm started!")
playsound("alarm.mp3")
