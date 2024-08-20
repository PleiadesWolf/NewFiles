import subprocess

while True:
    subprocess.run("su", "wolf")
    inpt = input ("Input: ")
    command = (inpt)
    if command == "htop":
        print("Permission Denied")
    else:
        subprocess.run(command)