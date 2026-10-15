import mysql.connector

con=mysql.connector.connect(
host="localhost",
user="root",
password="K9#mQ!8xL2$vW7*p",
database="student_db"
)

cursor=con.cursor()

sid=input("Student ID: ")

cursor.execute(
"SELECT marks FROM marks WHERE student_id=%s",
(sid,)
)

data=cursor.fetchall()

total=0

for row in data:
    total=total+row[0]

subjects=len(data)

percentage=total/subjects

print("Total:",total)
print("Percentage:",percentage)