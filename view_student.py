from database import cursor

query = "SELECT * FROM students"

cursor.execute(query)

data = cursor.fetchall()

for row in data:
    print(row)