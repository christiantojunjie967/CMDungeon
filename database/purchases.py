
from database.connection import get_connection


def purchaseItem(playerID, itemID):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Retrieve item information
        cursor.execute("""
            SELECT *
            FROM items
            WHERE item_id = ?
        """, (itemID,))

        item = cursor.fetchone()

        if item is None:
            return False, "Item not found!"

        price = item["price"]

        # Check player gold
        cursor.execute("""
            SELECT gold
            FROM players
            WHERE player_id = ?
        """, (playerID,))

        player = cursor.fetchone()

        if player is None:
            return False, "Player not found!"

        if player["gold"] < price:
            return False, "You don't have enough Gold!"

        # Deduct gold
        cursor.execute("""
            UPDATE players
            SET gold = gold - ?
            WHERE player_id = ?
        """, (price, playerID))

        # Add item to inventory or increase its quantity
        cursor.execute("""
            INSERT INTO inventory (
                player_id,
                item_id,
                quantity,
                equipped
            )
            VALUES (?, ?, 1, 0)

            ON CONFLICT(player_id, item_id)
            DO UPDATE SET quantity = quantity + 1
        """, (playerID, itemID))

        connection.commit()

        return True, f"You purchased {item['item_name']}!"

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
