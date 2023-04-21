import sqlite3

filename = "coffeehouse_supplies.csv"
table_structure = """CREATE TABLE IF NOT EXISTS Coffee 
                  (ProductID INTEGER PRIMARY KEY NOT NULL, 
                  Product TEXT, Category TEXT, Supplier TEXT)"""
insert_data = "INSERT INTO Coffee (Product, Category, Supplier) VALUES (?, ?, ?)"

try:

    conn = sqlite3.connect("coffee.db")

    cursor = conn.cursor()

    cursor.execute(table_structure)

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            fields = line.strip().split(",")
            cursor.execute(insert_data, (fields[0], fields[1], fields[2]))

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM Coffee")
    count = cursor.fetchone()[0]
    print(f"{count} records successfully added to the Coffee table.")

except sqlite3.Error as error:

    print("Error:", error)

finally:

    conn.close()
