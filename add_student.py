from database import con,cursor

name = input("Enter Name: ")
roll = input("Enter Roll No: ")
branch = input("Enter Branch: ")
phone = input("Enter Phone: ")

query = """
INSERT INTO students
(name,roll_no,branch,phone)
VALUES (%s,%s,%s,%s)
"""

values = (name,roll,branch,phone)

cursor.execute(query,values)

con.commit()

print("Student Added Successfully")