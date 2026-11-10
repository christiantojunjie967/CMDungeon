from utils import clearScreen
from new_update import comingSoon
import time

def Tavern():
    clearScreen()
    Tavern = True
    while Tavern:
        print("===Tavern===")
        print("Tavern Owner: welcome Traveller, what do you need in our humble abode")
        print("1. Need new Quest")
        print("2. Need a room to rest")
        print("3. Nevermind")
        playerChoice = input("I think ")
        if playerChoice == "1":
            print("Tavern Owner: alright the quests are at the board on the left")
            time.sleep(3)
            print("Going to The Quest Board...")
            comingSoon()
        elif playerChoice == "2":
            print("Tavern Owner: Ok, we got a room for you Traveller")
            time.sleep(3)
            print("Going to The Room...")
            comingSoon()
        elif playerChoice == "3":
            print("Tavern Owner: Well then hope not bothering you too long")
            time.sleep(3)
            print("Leaving the Tavern...")
            Tavern = False
        else :
            print("Tavern Owner: what are you saying dear Traveller?")
            time.sleep(3)
            clearScreen()
            continue 
