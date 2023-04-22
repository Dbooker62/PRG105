import sqlite3


conn = sqlite3.connect('pets.db')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS Owners (OwnerID INTEGER PRIMARY KEY NOT NULL, OwnerName TEXT, OwnerPhone TEXT)""")


c.execute("""CREATE TABLE IF NOT EXISTS Pets (PetID INTEGER PRIMARY KEY NOT NULL, PetName TEXT, PetType TEXT, PetBreed TEXT, OwnerID INTEGER, FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID))""")


with open('Owners.txt', 'r') as f:
    owners = [tuple(line.strip().split(',')) for line in f.readlines()]

c.executemany("INSERT INTO Owners (OwnerName, OwnerPhone) VALUES (?, ?)", owners)


with open('Pets.txt', 'r') as f:
    pets = [tuple(line.strip().split(',')) for line in f.readlines()]

c.executemany("INSERT INTO Pets (PetName, PetType, PetBreed, OwnerID) VALUES (?, ?, ?, ?)", pets)


conn.commit()


c.execute("SELECT * FROM Owners")
owners = c.fetchall()

for owner in owners:
    print(f"Owner: {owner[1]} ({owner[2]})")
    c.execute("SELECT * FROM Pets WHERE OwnerID = ?", (owner[0],))
    pets = c.fetchall()
    for pet in pets:
        print(f"    Pet: {pet[1]}, Type: {pet[2]}, Breed: {pet[3]}")
      

conn.close()
