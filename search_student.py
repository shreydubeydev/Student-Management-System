import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="K9#mQ!8xL2$vW7*p",
    database="student_db"
)

cursor = con.cursor()

roll = input("Enter Roll Number: ")

cursor.execute(
    "SELECT * FROM students WHERE roll_no=%s",
    (roll,)
)

student = cursor.fetchone()

print(student)