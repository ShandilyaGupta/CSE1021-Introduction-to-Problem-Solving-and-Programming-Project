class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, _class, section, marks):
        student = {
            'Name': name,
            'Roll Number': roll_number,
            'Class': _class,
            'Section': section,
            'Marks': marks
        }
        self.students.append(student)
        print(f"Student {name} added successfully.")

    def view_student(self, roll_number):
        for student in self.students:
            if student['Roll Number'] == roll_number:
                print("\nStudent Details:")
                for key, value in student.items():
                    print(f"{key}: {value}")
                return
        print(f"Student with Roll Number {roll_number} not found.")

    def update_student(self, roll_number, new_name, new_class, new_section, new_marks):
        for student in self.students:
            if student['Roll Number'] == roll_number:
                student['Name'] = new_name
                student['Class'] = new_class
                student['Section'] = new_section
                student['Marks'] = new_marks
                print(f"Student {new_name}'s record updated successfully.")
                return
        print(f"Student with Roll Number {roll_number} not found.")

    def delete_student(self, roll_number):
        for student in self.students:
            if student['Roll Number'] == roll_number:
                self.students.remove(student)
                print(f"Student with Roll Number {roll_number} deleted successfully.")
                return
        print(f"Student with Roll Number {roll_number} not found.")

    def calculate_total_marks(self, roll_number):
        for student in self.students:
            if student['Roll Number'] == roll_number:
                total_marks = sum(student['Marks'].values())
                print(f"Total Marks for {student['Name']}: {total_marks}")
                return
        print(f"Student with Roll Number {roll_number} not found.")

    def calculate_average_marks(self, _class):
        total_marks = 0
        count = 0
        for student in self.students:
            if student['Class'] == _class:
                total_marks += sum(student['Marks'].values())
                count += 1
        if count > 0:
            average_marks = total_marks / count
            print(f"Average Marks for Class {_class}: {average_marks}")
        else:
            print(f"No students found in Class {_class}.")

    def generate_report(self):
        print("\nStudent Report:")
        for student in self.students:
            print("\nStudent Details:")
            for key, value in student.items():
                print(f"{key}: {value}")

def display_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Calculate Total Marks")
    print("6. Calculate Average Marks")
    print("7. Generate Report")
    print("8. Exit")

def main():
    sms = StudentManagementSystem()
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            _class = input("Enter class: ")
            section = input("Enter section: ")
            marks = {}
            subjects = input("Enter subjects (comma-separated): ").split(',')
            for subject in subjects:
                marks[subject.strip()] = int(input(f"Enter marks for {subject.strip()}: "))
            sms.add_student(name, roll_number, _class, section, marks)
        elif choice == '2':
            roll_number = input("Enter roll number of the student: ")
            sms.view_student(roll_number)
        elif choice == '3':
            roll_number = input("Enter roll number of the student to update: ")
            new_name = input("Enter new name: ")
            new_class = input("Enter new class: ")
            new_section = input("Enter new section: ")
            new_marks = {}
            subjects = input("Enter new marks for subjects (comma-separated): ").split(',')
            for subject in subjects:
                new_marks[subject.strip()] = int(input(f"Enter new marks for {subject.strip()}: "))
            sms.update_student(roll_number, new_name, new_class, new_section, new_marks)
        elif choice == '4':
            roll_number = input("Enter roll number of the student to delete: ")
            sms.delete_student(roll_number)
        elif choice == '5':
            roll_number = input("Enter roll number of the student: ")
            sms.calculate_total_marks(roll_number)
        elif choice == '6':
            _class = input("Enter class: ")
            sms.calculate_average_marks(_class)
        elif choice == '7':
            sms.generate_report()
        elif choice == '8':
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
if __name__ == "__main__":
    main()

