import time, subprocess
from random import randrange
sleep = time.sleep
file = '4569580598591488.wav'
try:
    import winsound
except ModuleNotFoundError:
    pass

while True:
    randnum = randrange(100)
    n = randnum
    if randnum > 95:
        print("Above 90. Number is:", n)
        winsound.PlaySound("4569580598591488.wav", winsound.SND_FILENAME)
        time.sleep(10)
    else:
        print("Number below requirements. Number is: ", n)
        time.sleep(120)