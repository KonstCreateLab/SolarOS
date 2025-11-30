import os
from datetime import datetime




print("SolarOS 1.20.0")
print("Waiting for user input...")



# mainloop
for z in range (100):
    action = input("SolarOS>")
    if action == ("help"):
        print("Currently is running SolarOS version 1.20.0\n Help commands:\n  cls - Clears screen.\n info: Shows more info about SolarOS. \n cmd - Starts windows cmd \n time - Shows current time.")
    if action == ("cls"):
        for i in range(100):
            print()
    if action == ("info"):
        print("SolarOS is created with python and created by KonstCreateLab")
    if action == ("cmd"):
        os.system("start")
    if action == ("time"):
        now = datetime.now()
        print("Time:")
        print(now)
    if action == ("exit"):
        quit()
