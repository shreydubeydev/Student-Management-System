import mysql.connector

con=mysql.connector.connect(
host="localhost",
user="root",
password="K9#mQ!8xL2$vW7*p",
database="student_db"
)

cursor=con.cursor()

student_id=input("Student ID: ")
subject=input("Subject: ")
marks=input("Marks: ")

query="""
INSERT INTO marks
(student_id,subject,marks)
VALUES(%s,%s,%s)
"""

cursor.execute(
query,
(student_id,subject,marks)
)

con.commit()

print("Marks Saved")