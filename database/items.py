
from database.connection import get_connection


# =====================================
# GET ALL ITEMS BY TYPE
# =====================================
def getItemsByType(itemType):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM items
        WHERE item_type = ?
        ORDER BY price ASC
    """, (itemType,))

    items = cursor.fetchall()
    connection.close()

    return items


# =====================================
# GET ITEM BY ID
# =====================================
def getItemByID(itemID):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM items
        WHERE item_id = ?
    """, (itemID,))

    item = cursor.fetchone()
    connection.close()

    return item


# =====================================
# GET ITEM BY NAME
# =====================================
def getItemByName(itemName):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM items
        WHERE item_name = ?
    """, (itemName,))

    item = cursor.fetchone()
    connection.close()

    return item
