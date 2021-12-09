# basic input, output programming
import time, os, sys

# delay/typing output effect
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

# delay/typing input effect
def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

# clear screen
def clearScreen():
    os.system("clear")