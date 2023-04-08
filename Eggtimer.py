import time
import pyttsx3

engine = pyttsx3.init()

time_in_seconds = int(input("Time in seconds: "))

for i in range(time_in_seconds, 0, -1):
    print(i)
    time.sleep(1)

text = "Eggs are done, please turn off the stove."
engine.say(text)
engine.runAndWait()
