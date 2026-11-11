from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SESSION_FILE = BASE_DIR / "player_session.txt"


def savePlayerSession(playerID):
    with open(SESSION_FILE, "w") as file:
        file.write(str(playerID))


def loadPlayerSession():
    if not SESSION_FILE.exists():
        return None

    try:
        with open(SESSION_FILE, "r") as file:
            return int(file.read().strip())

    except (ValueError, OSError):
        return None