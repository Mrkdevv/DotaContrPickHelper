import sqlite3

connection = sqlite3.connect('dota.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')


with open('Dota2Heroes.txt', 'r' , encoding="utf-8") as file:
    heroes = file.readlines()

for hero in heroes:
    hero = hero.strip()

    if hero:
        cursor.execute(
        "INSERT OR IGNORE INTO Heroes (name) VALUES (?)",
        (hero,)
        )



cursor.execute('''
CREATE TABLE IF NOT EXISTS Counterpicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hero_id INTEGER UNIQUE,
    first TEXT,
    second TEXT,
    third TEXT,
    FOREIGN KEY (hero_id) REFERENCES Heroes(id)
)
''')

with open('Dota2HeroesContrPick.txt', 'r' , encoding="utf-8") as file:
    lines = file.readlines()
    for hero_id , line in enumerate(lines , start=1):
        parts = [name.strip() for name in line.split(',')]
        if len(parts) == 3:
            cursor.execute(
                "INSERT OR IGNORE INTO Counterpicks (hero_id, first, second, third) VALUES (?, ?, ?, ?)",
                (hero_id, parts[0], parts[1], parts[2])
            )

connection.commit()
connection.close()