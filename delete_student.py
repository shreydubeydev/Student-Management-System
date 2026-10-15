from database import con,cursor

id = input("Enter Student ID: ")

query = "DELETE FROM students WHERE id=%s"

cursor.execute(query,(id,))
con.commit()

print("Deleted Successfully")