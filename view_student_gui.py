from tkinter import *
from tkinter import ttk

from database import cursor

root = Tk()

root.title("View Students")
root.geometry("900x400")

table = ttk.Treeview(
    root,
    columns=("ID","Name","Roll","Branch","Phone"),
    show="headings"
)

table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Roll", text="Roll Number")
table.heading("Branch", text="Branch")
table.heading("Phone", text="Phone")

table.column("ID", width=50)
table.column("Name", width=150)
table.column("Roll", width=100)
table.column("Branch", width=100)
table.column("Phone", width=150)

table.pack(fill=BOTH, expand=True)

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for row in students:
    table.insert("", END, values=row)

root.mainloop()