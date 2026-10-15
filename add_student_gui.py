from tkinter import *
from tkinter import messagebox
from database import con, cursor
def save_student():

    student_name = name.get()
    student_roll = roll.get()
    student_branch = branch.get()
    student_phone = phone.get()

    query = """
    INSERT INTO students
    (name, roll_no, branch, phone)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            student_name,
            student_roll,
            student_branch,
            student_phone
        )
    )

    con.commit()
    name.delete(0, END)
    roll.delete(0, END)
    branch.delete(0, END)
    phone.delete(0, END)

    messagebox.showinfo(
    "Success",
    "Student Added Successfully"
)
root = Tk()

root.title("Add Student")
root.geometry("500x400")

Label(root,text="Name").pack()

name = Entry(root,width=40)
name.pack()

Label(root,text="Roll Number").pack()

roll = Entry(root,width=40)
roll.pack()

Label(root,text="Branch").pack()

branch = Entry(root,width=40)
branch.pack()

Label(root,text="Phone").pack()

phone = Entry(root,width=40)
phone.pack()

Button(
    root,
    text="Save",
    command=save_student
).pack(pady=20)


root.mainloop()