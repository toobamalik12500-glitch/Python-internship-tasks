import json

students = []


# Save students to file
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


# Load students from file
def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = []


# Task 1 - Add Student
def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    save_students()

    print("\nStudent added successfully!")
    input("Press Enter to go back to menu...")


# Task 2 - View All Students
def view_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students found.")
    else:
        for i, student in enumerate(students, 1):
            print(i, ". Name:", student["name"])
            print("   Roll Number:", student["roll_number"])
            print("   Marks:", student["marks"])
            print("   Grade:", student["grade"])
            print("-" * 20)

    input("Press Enter to go back to menu...")


# Task 3 - Search Student
def search_student():
    roll_number = input("Enter roll number to search: ")
    found = False

    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])
            found = True
            break

    if not found:
        print("Student not found.")

    input("Press Enter to go back to menu...")


# Task 4 - Update Student
def update_student():
    roll_number = input("Enter roll number to update: ")

    for student in students:
        if student["roll_number"] == roll_number:
            student["name"] = input("Enter new name: ")
            student["marks"] = float(input("Enter new marks: "))

            if student["marks"] >= 80:
                student["grade"] = "A"
            elif student["marks"] >= 70:
                student["grade"] = "B"
            elif student["marks"] >= 60:
                student["grade"] = "C"
            elif student["marks"] >= 50:
                student["grade"] = "D"
            else:
                student["grade"] = "F"

            save_students()

            print("\nStudent updated successfully!")
            input("Press Enter to go back to menu...")
            return

    print("Student not found.")
    input("Press Enter to go back to menu...")


# Task 5 - Delete Student
def delete_student():
    roll_number = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            save_students()

            print("\nStudent deleted successfully!")
            input("Press Enter to go back to menu...")
            return

    print("Student not found.")
    input("Press Enter to go back to menu...")


# Task 6 - Calculate Average Marks
def calculate_average():
    if len(students) == 0:
        print("No students found.")
    else:
        total = 0

        for student in students:
            total = total + student["marks"]

        average = total / len(students)
        print("\nAverage marks:", average)

    input("Press Enter to go back to menu...")


# Load saved students
load_students()


# Main Menu
while True:
    print("\n------ Student Management System------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        calculate_average()
    elif choice == "7":
        print("Program ended. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")