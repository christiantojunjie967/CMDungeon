
from utils import clearScreen
from database.items import getItemsByType
from database.purchases import purchaseItem
from database.player_data import getPlayerGold

import time


def weaponShop(playerID):
    atWeaponShop = True

    while atWeaponShop:
        clearScreen()

        # Retrieve weapons from database
        weapons = getItemsByType("Weapon")

        # Retrieve current player gold
        gold = getPlayerGold(playerID)

        print("================================")
        print("          WEAPON SHOP")
        print("================================")
        print(f"Your Gold: {gold}")
        print()

        for weapon in weapons:
            print(
                f"{weapon['item_id']}. "
                f"{weapon['item_name']} - "
                f"{weapon['price']} Gold"
            )

        print()
        print("0. Return")

        playerChoice = input("\nI want to buy: ")

        if playerChoice == "0":
            atWeaponShop = False
            continue

        # Validate player selection
        if not playerChoice.isdigit():
            print("\nInvalid choice!")
            time.sleep(2)
            continue

        itemID = int(playerChoice)

        # Find selected weapon
        selectedWeapon = None

        for weapon in weapons:
            if weapon["item_id"] == itemID:
                selectedWeapon = weapon
                break

        if selectedWeapon is None:
            print("\nWeapon not found!")
            time.sleep(2)
            continue

        # Confirm purchase
        print(f"\nPurchase {selectedWeapon['item_name']}?")
        print(f"Price: {selectedWeapon['price']} Gold")

        confirmation = input("[Y/N]: ").upper()

        if confirmation != "Y":
            print("\nPurchase cancelled!")
            time.sleep(2)
            continue

        # Execute purchase
        success, message = purchaseItem(playerID, itemID)

        print(f"\n{message}")

        time.sleep(2)
