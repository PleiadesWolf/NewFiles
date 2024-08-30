import time, subprocess, winsound, random
while True:
    n = random.randrange(100)
    if n > 95:
        print("Yes", n)
        winsound.PlaySound("sounds.wav", winsound.SND_FILENAME)
        time.sleep(10)
    else:
        print("No", n)
        time.sleep(1)
