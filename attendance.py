import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="K9#mQ!8xL2$vW7*p",
    database="student_db"
)

cursor=con.cursor()

student_id=input("Enter Student ID: ")
date=input("Enter Date (YYYY-MM-DD): ")
status=input("Present/Absent: ")

query="""
INSERT INTO attendance
(student_id,date,status)
VALUES(%s,%s,%s)
"""

cursor.execute(
query,
(student_id,date,status)
)

con.commit()

print("Attendance Saved")