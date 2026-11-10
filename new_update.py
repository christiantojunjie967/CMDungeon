
import time
from utils import clearScreen

def comingSoon():
    newUpdate = True
    clearScreen()

    print("================================")
    print("         NEW UPDATE")
    print("================================")
    print()
    print("        Coming Soon! ")
    print()
    print("This feature is currently")
    print("under development.")
    print()
    print("Returning...")

    time.sleep(5)
    clearScreen()
    newUpdate = False