while True:

    print("\n1.Add Student")
    print("2.View Student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        import add_student

    elif choice == "2":
        import view_student

    elif choice == "3":
        import update_student

    elif choice == "4":
        import delete_student

    elif choice == "5":
        break