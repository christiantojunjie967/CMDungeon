from utils import clearScreen
from new_update import comingSoon

def Blacksmith():
    Blacksmith = True
    while Blacksmith:
        print("===Blacksmith===")
        print("Blacksmith: Welcome Player! what do you need?")
        print("1. Create Weapon")
        print("2. Upgrade Weapon")
        print("3. Leave Shop")
        playerChoice = input("well...")
        if playerChoice == "1":
            print("Travelling...")
            clearScreen(3)
            comingSoon()
        elif playerChoice == "2":
            print("Travelling...")
            clearScreen(3)
            comingSoon()
        elif playerChoice == "3":
            print("Leaving the Shop...")
            clearScreen(3)
            Blacksmith = False
        else :
            print("Not a Valid Input")
            clearScreen(3)
            continue