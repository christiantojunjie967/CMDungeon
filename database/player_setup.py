from database.players import createPlayer, loadPlayer
from database.player_session import (
    savePlayerSession,
    loadPlayerSession
)


def initializePlayer():
    playerID = loadPlayerSession()

    if playerID is not None:
        player = loadPlayer(playerID)

        if player is not None:
            print(f"Welcome back, {player['player_name']}!")
            return player

    print("================================")
    print("       CHARACTER CREATION")
    print("================================")

    playerName = input("Enter your character name: ").strip()

    while not playerName:
        print("Name cannot be empty!")
        playerName = input("Enter your character name: ").strip()

    playerID = createPlayer(playerName)

    savePlayerSession(playerID)

    return loadPlayer(playerID)