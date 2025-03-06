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
    student1 = Student("Aarav", 101, 85)
    student2 = Student("Aditya", 102, 90)
    student3 = Student("Rohan", 103, 78)

    print("Displaying initial student details:")
    student1.display_details()
    student2.display_details()
    student3.display_details()

    print("\nUpdating marks for Aarav:")
    student1.update_marks(95)

    print("\nDisplaying updated student details:")
    student1.display_details()

    print("\nUpdating marks for a student via user input:")
    roll_number = int(input("Enter roll number of the student to update marks: "))
    new_marks = float(input(f"Enter new marks for roll number {roll_number}: "))

    students = [student1, student2, student3]
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
