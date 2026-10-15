import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="K9#mQ!8xL2$vW7*p",
    database="student_db"
)

cursor = con.cursor()

username = input("Enter Username: ")
password = input("Enter Password: ")

query = """
SELECT * FROM users
WHERE username=%s AND password=%s
"""

cursor.execute(query, (username, password))

user = cursor.fetchone()

if user:
    print("✅ Login Successful")
else:
    print("❌ Invalid Username or Password")
