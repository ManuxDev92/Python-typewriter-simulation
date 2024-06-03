import sys
from time import sleep
import time 

def harry_styles(): 
    lines = [
        ("We don't talk enough", 0.15),
        ("We should open up", 0.15),
        ("Before it's all too much", 0.12),
        ("Will we ever learn?", 0.16),
        ("We've been here before", 0.15),
        ("It's just what we know", 0.12),
        ("Stop your crying, baby", 0.09),
        ("It's a sign of the times", 0.07), 
        ("We gotta get away", 0.09),
        ("We got to get away", 0.09),
        ("We got to get away...", 0.09) ]

    delays = [1, 1.4, 4, 1.9, 0.8, 5, 0.4, 2.4, 2, 2, 1]

    for i, (line, char_delay) in enumerate(lines): 
        for char in line: 
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print("")
        

harry_styles()