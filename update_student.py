from database import con,cursor

id = input("Enter Student ID: ")
phone = input("New Phone Number: ")

query = """
UPDATE students
SET phone=%s
WHERE id=%s
"""

cursor.execute(query,(phone,id))
con.commit()

print("Updated Successfully")