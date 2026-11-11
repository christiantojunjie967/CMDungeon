
from database.connection import get_connection


# =====================================
# GET PLAYER GOLD
# =====================================
def getPlayerGold(playerID):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT gold
        FROM players
        WHERE player_id = ?
    """, (playerID,))

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return None

    return result["gold"]


# =====================================
# UPDATE PLAYER GOLD
# =====================================
def updatePlayerGold(playerID, amount):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE players
        SET gold = gold + ?
        WHERE player_id = ?
          AND gold + ? >= 0
    """, (amount, playerID, amount))

    success = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return success


# =====================================
# GET PLAYER STATS
# =====================================
def getPlayerStats(playerID):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM player_stats
        WHERE player_id = ?
    """, (playerID,))

    stats = cursor.fetchone()
    connection.close()

    return stats


# =====================================
# ADD EXPERIENCE
# =====================================
def addExperience(playerID, amount):
    if amount < 0:
        return False

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE players
        SET experience = experience + ?
        WHERE player_id = ?
    """, (amount, playerID))

    success = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return success


# =====================================
# UPDATE PLAYER LEVEL
# =====================================
def updatePlayerLevel(playerID, newLevel):
    if newLevel < 1:
        return False

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE players
        SET level = ?
        WHERE player_id = ?
    """, (newLevel, playerID))

    success = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return success
