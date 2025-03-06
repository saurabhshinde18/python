class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks for {self.name} have been updated to {self.marks}")


def main():
    print("Enter number of students:")
    n = int(input())

    students = []

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}:")
        name = input("Enter name: ")
        roll_number = int(input("Enter roll number: "))
        marks = float(input("Enter marks: "))
        
        student = Student(name, roll_number, marks)
        students.append(student)

    print("\nDisplaying initial student details:")
    for student in students:
        student.display_details()

    print("\nUpdating marks for a student:")
    roll_number = int(input("Enter roll number of the student to update marks: "))
    new_marks = float(input(f"Enter new marks for roll number {roll_number}: "))

    for student in students:
        if student.roll_number == roll_number:
            student.update_marks(new_marks)
            break
    else:
        print("Student with this roll number not found.")

    print("\nDisplaying final student details:")
    for student in students:
        student.display_details()


if __name__ == "__main__":
    main()
