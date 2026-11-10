
from utils import clearScreen
import time

# Temporary player data
gold = 1000
armor_inventory = []


def armorShop():
    atArmorShop = True

    while atArmorShop:
        clearScreen()

        print("================================")
        print("          ARMOR SHOP")
        print("================================")
        print(f"Your Gold: {gold}")
        print()
        print("1. Leather Armor  - 100 Gold")
        print("2. Iron Armor     - 300 Gold")
        print("3. Steel Armor    - 600 Gold")
        print("4. Return")

        playerChoice = input("\nI want to buy: ")

        if playerChoice == "1":
            buyArmor("Leather Armor", 100)

        elif playerChoice == "2":
            buyArmor("Iron Armor", 300)

        elif playerChoice == "3":
            buyArmor("Steel Armor", 600)

        elif playerChoice == "4":
            atArmorShop = False

        else:
            print("Invalid choice!")
            time.sleep(2)


def buyArmor(armorName, price):
    global gold

    if gold >= price:
        gold -= price
        armor_inventory.append(armorName)

        print(f"\nYou purchased {armorName}!")
        print(f"Remaining Gold: {gold}")

    else:
        print("\nYou don't have enough Gold!")

    time.sleep(2)
