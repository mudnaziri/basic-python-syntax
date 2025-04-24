def add_student(students):
    print("__Add New Student__")
    name = input("Enter name: ")
    age = input("Enter age: ")
    roll = input("Enter roll number: ")
    email = input("Enter email: ")
    course = input("Enter course: ")
    skills = input("Enter skills (comma separated): ").split(",")

    student = {
        "name": name.strip(),
        "age": age.strip(),
        "roll_number": roll.strip(),
        "email": email.strip(),
        "course": course.strip(),
        "skills": [skill.strip() for skill in skills]
    }

    students.append(student)
    print("__Student added successfully__")


def view_student(students):
    print("__View Students__")
    if not students:
        print("No student found.")
        return

    for n, student in enumerate(students, 1):
        print(f"\nStudent {n}")
        for key, value in student.items():
            print(f'{key.capitalize()}: {value}')


def search_student(students):
    ro_num = input("Enter roll number: ").strip()
    found = False
    for student in students:
        if student["roll_number"] == ro_num:
            print("\nStudent Found:")
            for key, value in student.items():
                print(f"{key.capitalize()}: {value}")
            found = True
            break

    if not found:
        print("Student not found.")


def delete_student(students):
    print("__Delete Student__")
    ro_num = input("Enter roll number: ").strip()
    for i, student in enumerate(students):
        if student["roll_number"] == ro_num:
            del students[i]
            print("Account deleted successfully.")
            return
    print("Student not found.")


def update_student(students):
    print("__Update Student Account__")
    ro_num = input("Enter roll number: ").strip()
    for student in students:
        if student["roll_number"] == ro_num:
            print("1. Update Age")
            print("2. Update Course")
            print("3. Update Email")
            choice = input("Choose an option: ")

            if choice == "1":
                student["age"] = input("Enter new age: ").strip()
            elif choice == "2":
                student["course"] = input("Enter new course: ").strip()
            elif choice == "3":
                student["email"] = input("Enter new email: ").strip()
            else:
                print("Invalid option.")

            print("Student account updated successfully.")
            return

    print("Student not found.")


def student_portal():
    students = []
    while True:
        print("\n==== Student Profile Management System ====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search by Roll Number")
        print("4. Update Student Profile")
        print("5. Delete Profile")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print(" Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    student_portal()
