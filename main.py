students = []


def add_student():
    roll = input("Enter roll number:")
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    students.append((roll, name, marks))
    print("Student added successfully.")


def view_students():
    print("\Student Records:")
    for s in students:
        print(f"Roll Number: {s[0]}, Name: {s[1]}, Marks: {s[2]}")


def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    for s in students:
        if s[0] == roll:
            print("Student found:")
            print(f"Roll Number: {s[0]}, Name: {s[1]}, Marks: {s[2]}")
            found = True
            break
        if not found:
            print("Student not found.")
            
            
def delete_student():
    roll = input("Enter roll number to delete: ")
    found = False
    for s in students:
        if s[0] == roll:
            students.remove(s)
            print("Student deleted successfully.")
            found = True
            break
        if not found:
            print("Student not found.") 
            
            
def update_student():
    roll = input("Enter roll number to update: ")
    found = False
    for i in range(len(students)):
        if students[i][0] == roll:
            name = input("Enter new student name: ")
            marks = float(input("Enter new student marks: "))
            students[i] = (roll, name, marks)
            print("Student updated successfully.")
            found = True
            break
        if not found:
            print("Student not found.")
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. delete Student")
    print("5. Update Student")
    print("6. Exit")
    
    
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        update_student()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")  