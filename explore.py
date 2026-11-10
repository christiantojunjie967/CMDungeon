from utils import clearScreen
from new_update import comingSoon
import time

def explore():
    explore = True
    clearScreen()
    while explore:
        print("===Explore===")
        print("You opened the map and there is places you can go")
        print("1. Forest")
        print("2. Cave")
        print("3. Main City")
        playerChoice = input("you went to ")
        if playerChoice == "1":
            print("You are travelling...")
            clearScreen(3)
            comingSoon()
        elif playerChoice == "2":
            print("You are travelling...")
            clearScreen(3)
            comingSoon()
        elif playerChoice == "3":
            print("You are travelling...")
            clearScreen(3)
            explore = False
        else :
            print("You definitely an idiot")
            time.sleep (6)
            print("Recovering yourself...")
            clearScreen(3)
            continue
