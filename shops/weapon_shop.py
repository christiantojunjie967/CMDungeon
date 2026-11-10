from utils import clearScreen
import time

# Temporary player data
gold = 1000
weapon_inventory = []

def weaponShop():
    atWeaponShop = True

    while atWeaponShop:
        clearScreen()

        print("================================")
        print("          WEAPON SHOP")
        print("================================")
        print(f"Your Gold: {gold}")
        print()
        print("1. Wooden Sword  - 100 Gold")
        print("2. Iron Sword    - 300 Gold")
        print("3. Steel Sword   - 600 Gold")
        print("4. Return")

        playerChoice = input("\nI want to buy: ")

        if playerChoice == "1":
            buyWeapon("Wooden Sword", 100)

        elif playerChoice == "2":
            buyWeapon("Iron Sword", 300)

        elif playerChoice == "3":
            buyWeapon("Steel Sword", 600)

        elif playerChoice == "4":
            atWeaponShop = False

        else:
            print("\nInvalid choice!")
            time.sleep(2)


def buyWeapon(weaponName, price):
    global gold

    if gold >= price:
        gold -= price
        weapon_inventory.append(weaponName)

        print(f"\nYou purchased {weaponName}!")
        print(f"Remaining Gold: {gold}")

    else:
        print("\nYou don't have enough Gold!")

    time.sleep(2)