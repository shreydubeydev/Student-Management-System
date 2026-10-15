from tkinter import *

root = Tk()

root.title("Student Management System")
root.geometry("700x500")

heading = Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial",20,"bold")
)

heading.pack(pady=20)

def open_add_student():

    import add_student_gui
def open_view_students():

    import view_student_gui
Button(
    root,
    text="Add Student",
    width=25,
    height=2,
    command=open_add_student
).pack(pady=5)
Button(
    root,
    text="View Students",
    width=25,
    height=2,
    command=open_view_students
).pack(pady=5)

Button(root,text="Search Student",width=25,height=2).pack(pady=5)

Button(root,text="Attendance",width=25,height=2).pack(pady=5)

Button(root,text="Add Marks",width=25,height=2).pack(pady=5)

Button(root,text="Result",width=25,height=2).pack(pady=5)

Button(root,text="Exit",width=25,height=2,
       command=root.destroy).pack(pady=5)

root.mainloop()