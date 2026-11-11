from database.connection import get_connection


def setupDatabase():
    connection = get_connection()
    cursor = connection.cursor()

    # ==============================
    # PLAYERS TABLE
    # ==============================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            player_id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            level INTEGER NOT NULL DEFAULT 1,
            experience INTEGER NOT NULL DEFAULT 0,
            gold INTEGER NOT NULL DEFAULT 100,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ==============================
    # PLAYER STATS TABLE
    # ==============================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_stats (
            player_id INTEGER PRIMARY KEY,
            base_hp INTEGER NOT NULL DEFAULT 100,
            bonus_hp INTEGER NOT NULL DEFAULT 0,
            base_physical_dmg INTEGER NOT NULL DEFAULT 10,
            bonus_physical_dmg INTEGER NOT NULL DEFAULT 0,
            base_magic_dmg INTEGER NOT NULL DEFAULT 0,
            bonus_magic_dmg INTEGER NOT NULL DEFAULT 0,
            base_physical_def INTEGER NOT NULL DEFAULT 5,
            bonus_physical_def INTEGER NOT NULL DEFAULT 0,
            base_magic_def INTEGER NOT NULL DEFAULT 5,
            bonus_magic_def INTEGER NOT NULL DEFAULT 0,

            FOREIGN KEY (player_id)
                REFERENCES players(player_id)
                ON DELETE CASCADE
        )
    """)

    # ==============================
    # ITEMS TABLE
    # ==============================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL UNIQUE,
            item_type TEXT NOT NULL
                CHECK (item_type IN ('Weapon', 'Armor', 'Potion', 'Other')),
            description TEXT,
            price INTEGER NOT NULL DEFAULT 0,
            attack_bonus INTEGER NOT NULL DEFAULT 0,
            defense_bonus INTEGER NOT NULL DEFAULT 0,
            hp_bonus INTEGER NOT NULL DEFAULT 0
        )
    """)

    # ==============================
    # INVENTORY TABLE
    # ==============================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL DEFAULT 1,
            equipped INTEGER NOT NULL DEFAULT 0
                CHECK (equipped IN (0, 1)),

            FOREIGN KEY (player_id)
                REFERENCES players(player_id)
                ON DELETE CASCADE,

            FOREIGN KEY (item_id)
                REFERENCES items(item_id),

            UNIQUE (player_id, item_id)
        )
    """)

    # ==============================
    # STARTER ITEMS
    # ==============================
    starter_items = [
        ("Wooden Sword", "Weapon", "A basic wooden sword.", 100, 5, 0, 0),
        ("Iron Sword", "Weapon", "A reliable iron sword.", 300, 15, 0, 0),
        ("Steel Sword", "Weapon", "A powerful steel sword.", 600, 30, 0, 0),

        ("Leather Armor", "Armor", "Basic leather protection.", 100, 0, 5, 0),
        ("Iron Armor", "Armor", "Solid iron protection.", 300, 0, 15, 0),
        ("Steel Armor", "Armor", "Strong steel protection.", 600, 0, 30, 0),

        ("Small Health Potion", "Potion", "Restores 25 HP.", 50, 0, 0, 25),
        ("Large Health Potion", "Potion", "Restores 100 HP.", 150, 0, 0, 100)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO items (
            item_name,
            item_type,
            description,
            price,
            attack_bonus,
            defense_bonus,
            hp_bonus
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, starter_items)

    connection.commit()
    connection.close()

    print("Database setup completed successfully!")


if __name__ == "__main__":
    setupDatabase()