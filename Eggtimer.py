import time
import pyttsx3

engine = pyttsx3.init()
time_in_minutes = int(input("Time in minutes: "))

time_in_seconds = time_in_minutes * 60
for i in range(time_in_seconds, 0, -1):
    print(i)
    time.sleep(1)

text = "Eggs are done, please turn off the stove."
engine.say(text)
engine.runAndWait()
