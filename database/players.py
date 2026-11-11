from database.connection import get_connection


def createPlayer(playerName):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO players (player_name)
            VALUES (?)
        """, (playerName,))

        playerID = cursor.lastrowid

        cursor.execute("""
            INSERT INTO player_stats (player_id)
            VALUES (?)
        """, (playerID,))

        connection.commit()

        print(f"\nWelcome, {playerName}!")
        return playerID

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def loadPlayer(playerID):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            players.*,
            player_stats.*
        FROM players
        JOIN player_stats
            ON players.player_id = player_stats.player_id
        WHERE players.player_id = ?
    """, (playerID,))

    player = cursor.fetchone()

    connection.close()

    return player