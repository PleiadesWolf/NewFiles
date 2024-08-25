import subprocess

while True:
    try:
        inpt = input("Input: ")
        command = (inpt)

        if command == "htop":
           print("Permission Denied")
    
        else:
           test = inpt.split(" ")
           subprocess.run(test)
    except EOFError:
        break


