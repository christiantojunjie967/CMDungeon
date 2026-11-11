
import time

from shop import shop
from utils import clearScreen
from Blacksmith import Blacksmith
from new_update import comingSoon
from Tavern import Tavern
from explore import explore

from database.player_setup import initializePlayer
from database.player_data import getPlayerGold


def main():
    # Initialize or load player from SQLite
    player = initializePlayer()
    playerID = player["player_id"]

    mainMenu = True

    while mainMenu:
        clearScreen()

        # Retrieve latest player information
        currentGold = getPlayerGold(playerID)

        print("================================")
        print("           MAIN CITY")
        print("================================")
        print(f"Welcome, {player['player_name']}!")
        print(f"Level: {player['level']}")
        print(f"Gold: {currentGold}")
        print()
        print("You have arrived at the main hub")
        print("of the city, dear traveller!")
        print()
        print("What do you want to do?")
        print("1. Go To Shop")
        print("2. Go To Blacksmith")
        print("3. Go To Dungeon")
        print("4. Go To Tavern")
        print("5. Go Explore")
        print("6. Exit Game")

        playerChoice = input("\nI Will: ")

        if playerChoice == "1":
            print("\nGoing to the Shopping District...")
            time.sleep(3)
            shop(playerID)

        elif playerChoice == "2":
            print("\nEntering the Blacksmith...")
            time.sleep(3)
            Blacksmith()

        elif playerChoice == "3":
            print("\nTravelling...")
            time.sleep(3)
            comingSoon()

        elif playerChoice == "4":
            print("\nEntering the Tavern...")
            time.sleep(3)
            Tavern()

        elif playerChoice == "5":
            print("\nTravelling to the City Gate...")
            time.sleep(3)
            explore()

        elif playerChoice == "6":
            print("\nYour progress is automatically saved.")
            choice = input("Are you sure you want to exit? [Y/N]: ").upper()

            if choice == "Y":
                print("\nThank you for playing newCMDungeon!")
                time.sleep(2)
                mainMenu = False

        else:
            print("\nNot a valid choice!")
            time.sleep(2)


if __name__ == "__main__":
    main()
