import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Swethaji@028",   # change if needed
    database="student_db"
)

cursor = conn.cursor()
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    course = input("Enter course: ")
    department = input("Enter department: ")
    marks = int(input("Enter marks: "))
    attendance = int(input("Enter attendance (%): "))
    email = input("Enter email: ")

    query = """INSERT INTO students 
    (name, age, gender, course, department, marks, attendance, email) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    cursor.execute(query, (name, age, gender, course, department, marks, attendance, email))
    conn.commit()

    print("Student added successfully!")
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
def update_student():
    student_id = int(input("Enter student ID: "))

    print("What do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Gender")
    print("4. Course")
    print("5. Department")
    print("6. Marks")
    print("7. Attendance")
    print("8. Email")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_value = input("Enter new name: ")
        query = "UPDATE students SET name=%s WHERE student_id=%s"

    elif choice == '2':
        new_value = int(input("Enter new age: "))
        query = "UPDATE students SET age=%s WHERE student_id=%s"

    elif choice == '3':
        new_value = input("Enter new gender: ")
        query = "UPDATE students SET gender=%s WHERE student_id=%s"

    elif choice == '4':
        new_value = input("Enter new course: ")
        query = "UPDATE students SET course=%s WHERE student_id=%s"

    elif choice == '5':
        new_value = input("Enter new department: ")
        query = "UPDATE students SET department=%s WHERE student_id=%s"

    elif choice == '6':
        new_value = int(input("Enter new marks: "))
        query = "UPDATE students SET marks=%s WHERE student_id=%s"

    elif choice == '7':
        new_value = int(input("Enter new attendance: "))
        query = "UPDATE students SET attendance=%s WHERE student_id=%s"

    elif choice == '8':
        new_value = input("Enter new email: ")
        query = "UPDATE students SET email=%s WHERE student_id=%s"

    else:
        print("Invalid choice")
        return

    cursor.execute(query, (new_value, student_id))
    conn.commit()

    print("Updated successfully!")
def delete_student():
    student_id = int(input("Enter student ID: "))

    # Check if student exists
    cursor.execute("SELECT * FROM students WHERE student_id=%s", (student_id,))
    result = cursor.fetchone()

    if result is None:
        print("Student not found!")
        return

    # Confirmation before delete
    confirm = input("Are you sure you want to delete this student? (yes/no): ")

    if confirm.lower() == 'yes':
        query = "DELETE FROM students WHERE student_id=%s"
        cursor.execute(query, (student_id,))
        conn.commit()
        print("Deleted successfully!")
    else:
        print("Deletion cancelled.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
