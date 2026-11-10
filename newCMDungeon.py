from shop import shop
from utils import clearScreen
from Blacksmith import Blacksmith
from new_update import comingSoon
from Tavern import Tavern
from explore import explore

# Player Data
playerLvl = 0
Experience = 0
gold = 10

baseHP = 100
basePysichalDmg = 10
baseMagicDmg = 0
basePhysicalDef = 5
baseMagicDef = 5

bonusHP = 0
bonusPysichalDmg = 0
bonusMagicDmg = 0
bonusPhysicalDef = 0
bonusMagicDef = 0

totalHP = baseHP + bonusHP
totalPysichalDmg = basePysichalDmg + bonusPysichalDmg
totalMagicDmg = baseMagicDmg + bonusMagicDmg
totalPhysicalDef = basePhysicalDef + bonusPhysicalDef
totalMagicDef = baseMagicDef + bonusMagicDef

def main():
    mainMenu = True
   
    while mainMenu:
        clearScreen()
        print("===Main City===")
        print("you had arrived at the main hub of the city, dear traveller!")
        print("what do you wanna do at the Main City?")
        print("1. Go To Shop")
        print("2. Go To Blacksmith")
        print("3. Go To Dungeon")
        print("4. Go To Tavern")
        print("5. Go Explore")
        print("6. Exit Game")
        playerChoice = input("I Will ")
        if playerChoice == "1":
            print("Going to the Shopping District...")
            clearScreen(3)
            shop()
        elif playerChoice == "2":
            print("Entering the Blacksmith...")
            clearScreen(3)
            Blacksmith()
        elif playerChoice == "3":
            print("Travelling...")
            clearScreen(3)
            comingSoon()
        elif playerChoice == "4":
            print("Entering the Tavern...")
            clearScreen(3)
            Tavern()
        elif playerChoice == "5":
            print("Travelling to the City Gate...")
            clearScreen(3)
            explore()
        elif playerChoice == "6":
            print("Unsaved Data will be loss are you sure?")
            print("[Y/N]")
            choice = input("").upper()
            if choice == "Y":
                break
            else:
                continue

        else:
            print("Not A Valid Choice")
            clearScreen(3)
            continue

if __name__ == "__main__" :
    main()
