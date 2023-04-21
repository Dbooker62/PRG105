import sqlite3


conn = sqlite3.connect("coffee.db")
cur = conn.cursor()


cur.execute("SELECT DISTINCT Category, Product FROM Coffee ORDER BY Category, Product")


results = cur.fetchall()


print("{:<20}{:<20}".format("Category", "Product"))
print("=" * 40)


for row in results:
    category, product = row
    print("{:<20}{:<20}".format(category, product))


conn.close()
