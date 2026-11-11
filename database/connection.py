import sqlite3
from pathlib import Path

# Get the main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database location
DATABASE_PATH = BASE_DIR / "newCMDungeon.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    # Enable foreign key relationships
    connection.execute("PRAGMA foreign_keys = ON")

    # Allow accessing columns by name
    connection.row_factory = sqlite3.Row

    return connection