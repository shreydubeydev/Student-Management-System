import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="K9#mQ!8xL2$vW7*p",
    database="student_db"
)

cursor = con.cursor()

print("Database Connected")