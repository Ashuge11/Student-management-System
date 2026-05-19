import pandas as pd
import numpy as np


# =========================
# STUDENT CLASS
# =========================

class Student:

    def __init__(self, rollno, name, marks, attendance):

        self.rollno = rollno
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def percentage(self):

        return np.mean(list(self.marks.values()))

    def grade(self):

        per = self.percentage()

        if per >= 90:
            return "A+"

        elif per >= 75:
            return "A"

        elif per >= 60:
            return "B"

        elif per >= 40:
            return "C"

        else:
            return "Fail"

    def display(self):

        print("\n========== STUDENT DETAILS ==========")

        print(f"Roll Number   : {self.rollno}")
        print(f"Name          : {self.name}")
        print(f"Marks         : {self.marks}")
        print(f"Attendance    : {self.attendance}%")
        print(f"Percentage    : {self.percentage():.2f}%")
        print(f"Grade         : {self.grade()}")


# =========================
# STUDENT LIST
# =========================

students = []


# =========================
# ADD STUDENT
# =========================

def add_student():

    roll = int(input("Enter Roll Number: "))

    name = input("Enter Student Name: ")

    subjects = ["Python", "Math", "History"]

    marks = {}

    for subject in subjects:

        score = int(input(f"Enter marks for {subject}: "))

        marks[subject] = score

    attendance = int(input("Enter Attendance %: "))

    student = Student(roll, name, marks, attendance)

    students.append(student)

    print("Student Added Successfully!")


# =========================
# VIEW STUDENTS
# =========================

def view_students():

    if len(students) == 0:

        print("No students found")
        return

    for student in students:

        student.display()


# =========================
# SEARCH STUDENT
# =========================

def search_student():

    if len(students) == 0:

        print("No students found")
        return

    roll = int(input("Enter Roll Number: "))

    for student in students:

        if student.rollno == roll:

            student.display()
            return

    print("Student not found")


# =========================
# DELETE STUDENT
# =========================

def delete_student():

    if len(students) == 0:

        print("No students found")
        return

    roll = int(input("Enter Roll Number: "))

    for student in students:

        if student.rollno == roll:

            students.remove(student)

            print("Student Deleted Successfully!")

            return

    print("Student not found")


# =========================
# RANK STUDENTS
# =========================

def rank_students():

    if len(students) == 0:

        print("No students found")
        return

    sorted_students = sorted(
        students,
        key=lambda x: x.percentage(),
        reverse=True
    )

    print("\n========== RANK LIST ==========")

    rank = 1

    for student in sorted_students:

        print(
            f"Rank {rank} : "
            f"{student.name} "
            f"({student.percentage():.2f}%)"
        )

        rank += 1


# =========================
# SUBJECT TOPPER
# =========================

def subject_topper():

    if len(students) == 0:

        print("No students found")
        return

    subject = input("Enter Subject Name: ")

    topper = None

    highest = -1

    for student in students:

        if subject in student.marks:

            if student.marks[subject] > highest:

                highest = student.marks[subject]

                topper = student

    if topper:

        print("\n========== SUBJECT TOPPER ==========")

        print(f"Subject       : {subject}")
        print(f"Topper Name   : {topper.name}")
        print(f"Roll Number   : {topper.rollno}")
        print(f"Marks         : {highest}")
        print(f"Percentage    : {topper.percentage():.2f}%")
        print(f"Grade         : {topper.grade()}")

    else:

        print("Subject not found")


# =========================
# EXPORT CSV
# =========================

def export_csv():

    if len(students) == 0:

        print("No students found")
        return

    data = []

    for student in students:

        row = {

            "Roll Number": student.rollno,
            "Name": student.name,
            "Attendance": student.attendance,
            "Percentage": round(student.percentage(), 2),
            "Grade": student.grade()

        }

        row.update(student.marks)

        data.append(row)

    df = pd.DataFrame(data)

    df.to_csv("report.csv", index=False)

    print("CSV Report Exported Successfully!")


# =========================
# ANALYTICS
# =========================

def analytics():

    if len(students) == 0:

        print("No students found")
        return

    percentages = []

    for student in students:

        percentages.append(student.percentage())

    print("\n========== ANALYTICS ==========")

    print(f"Average Percentage : {np.mean(percentages):.2f}")

    print(f"Highest Percentage : {np.max(percentages):.2f}")

    print(f"Lowest Percentage  : {np.min(percentages):.2f}")


# =========================
# MAIN MENU
# =========================

while True:

    print("""

========== SMART STUDENT MANAGEMENT ==========

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Rank Students
6. Subject Topper
7. Export CSV
8. Analytics
9. Exit

""")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        delete_student()

    elif choice == "5":

        rank_students()

    elif choice == "6":

        subject_topper()

    elif choice == "7":

        export_csv()

    elif choice == "8":

        analytics()

    elif choice == "9":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")