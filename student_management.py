# Student Management System
# Name: Abdul Wahid
# Reg No: B25F0416AI290
#
# A menu-driven program to add, view, search, update, and delete
# student records, with file handling so records are saved
# between runs of the program.

FILE_NAME = "students.txt"


# ---------------- FILE HANDLING ----------------

def load_students():
    """Read all student records from the file into a list of dictionaries."""
    students = []
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            student = {
                "id": parts[0],
                "name": parts[1],
                "age": int(parts[2]),
                "course": parts[3],
                "marks": [int(parts[4]), int(parts[5]), int(parts[6])]
            }
            students.append(student)
        file.close()
    except FileNotFoundError:
        # No file yet means no students saved so far
        students = []
    return students


def save_students(students):
    """Write all student records back to the file."""
    file = open(FILE_NAME, "w")
    for s in students:
        line = s["id"] + "," + s["name"] + "," + str(s["age"]) + "," + s["course"]
        line += "," + str(s["marks"][0]) + "," + str(s["marks"][1]) + "," + str(s["marks"][2])
        file.write(line + "\n")
    file.close()


# ---------------- FEATURE FUNCTIONS ----------------

def add_student(students):
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ")

    # check if ID already exists
    for s in students:
        if s["id"] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    print("Enter marks for 3 subjects (out of 100 each):")
    marks1 = int(input("Subject 1 marks: "))
    marks2 = int(input("Subject 2 marks: "))
    marks3 = int(input("Subject 3 marks: "))

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": [marks1, marks2, marks3]
    }

    students.append(new_student)
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    print("\n--- All Students ---")
    if len(students) == 0:
        print("No student records found.")
        return

    for s in students:
        total = sum(s["marks"])
        average = total / 3
        print("-" * 40)
        print("ID:", s["id"])
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Course:", s["course"])
        print("Marks:", s["marks"])
        print("Average:", round(average, 2))
    print("-" * 40)


def search_student(students):
    print("\n--- Search Student ---")
    search_id = input("Enter Student ID to search: ")

    for s in students:
        if s["id"] == search_id:
            print("Student Found:")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Course:", s["course"])
            print("Marks:", s["marks"])
            return

    print("No student found with ID:", search_id)


def update_student(students):
    print("\n--- Update Student ---")
    update_id = input("Enter Student ID to update: ")

    for s in students:
        if s["id"] == update_id:
            print("Leave field blank to keep the current value.")

            new_name = input("New Name (" + s["name"] + "): ")
            if new_name != "":
                s["name"] = new_name

            new_age = input("New Age (" + str(s["age"]) + "): ")
            if new_age != "":
                s["age"] = int(new_age)

            new_course = input("New Course (" + s["course"] + "): ")
            if new_course != "":
                s["course"] = new_course

            update_marks = input("Do you want to update marks? (yes/no): ")
            if update_marks.lower() == "yes":
                marks1 = int(input("Subject 1 marks: "))
                marks2 = int(input("Subject 2 marks: "))
                marks3 = int(input("Subject 3 marks: "))
                s["marks"] = [marks1, marks2, marks3]

            save_students(students)
            print("Student record updated successfully.")
            return

    print("No student found with ID:", update_id)


def delete_student(students):
    print("\n--- Delete Student ---")
    delete_id = input("Enter Student ID to delete: ")

    for s in students:
        if s["id"] == delete_id:
            confirm = input("Are you sure you want to delete " + s["name"] + "? (yes/no): ")
            if confirm.lower() == "yes":
                students.remove(s)
                save_students(students)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("No student found with ID:", delete_id)


def show_statistics(students):
    print("\n--- Class Statistics ---")
    if len(students) == 0:
        print("No student records found.")
        return

    all_averages = []
    for s in students:
        average = sum(s["marks"]) / 3
        all_averages.append(average)

    class_average = sum(all_averages) / len(all_averages)
    highest = max(all_averages)
    lowest = min(all_averages)

    # find the top performing student
    top_index = all_averages.index(highest)
    top_student = students[top_index]

    print("Class Average Marks:", round(class_average, 2))
    print("Highest Average Marks:", round(highest, 2))
    print("Lowest Average Marks:", round(lowest, 2))
    print("Top Performing Student:", top_student["name"], "(ID:", top_student["id"], ")")


# ---------------- MAIN MENU ----------------

def main():
    students = load_students()

    while True:
        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Class Statistics")
        print("7. Exit")
        print("==================================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_statistics(students)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
