from utils import clearScreen
from new_update import comingSoon
from utils import clearScreen
from shop import armorShop

def shop():
    atShop = True
    while atShop:
        clearScreen()
        print("===Shopping District===")
        print("what shop are you going to?")
        print("1. Armor Shop")
        print("2. Weapon Shop")
        print("3. Potion Shop")
        print("4. Back to Main City")
        playerChoice = input("I need to go to: ")
        if playerChoice == "1":
            print("Going to Armor Shop")
            clearScreen(3)
            armorShop()
        elif playerChoice =="2":
            print("Travelling...")
            clearScreen(3)
            comingSoon()
        elif playerChoice == "3":
            print("Travelling...")
            clearScreen(3)
            comingSoon()
        elif playerChoice == "4":
            print("Returning to Main City...")
            clearScreen(3)
            atShop = False
        else :
            print("not a valid input")
            clearScreen(3)
            continue


