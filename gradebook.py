class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, grade_item, grade):
        self.grades[grade_item] = grade

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.student_id})"

class GradeItem:
    def __init__(self, name, total_points):
        self.name = name
        self.total_points = total_points

    def __str__(self):
        return f"{self.name} ({self.total_points})"

class Course:
    def __init__(self):
        self.students = {}
        self.grade_items = {}
    def add_student(self, student):
        if student.student_id in self.students:
            print("Error: Student ID already exists.")
        else:
            self.students[student.student_id] = student
    def add_grade_item(self, grade_item):
        if grade_item.name in self.grade_items:
            print("Error: Grade item already exists.")
        else:
            self.grade_items[grade_item.name] = grade_item
    def add_student_grade(self, grade_item_name, student_id, grade):
        if student_id not in self.students:
            print(f"Error: No student with ID {student_id}.")
            return
        if grade_item_name not in self.grade_items:
            print(f"Error: No grade item named {grade_item_name}.")
            return
        grade_item = self.grade_items[grade_item_name]
        if not (0 <= grade <= grade_item.total_points):
            print(f"Error: Grade must be between 0 and {grade_item.total_points}.")
            return
        student = self.students[student_id]
        student.add_grade(grade_item_name, grade)
    def print_student_grades(self, student_id):
        if student_id not in self.students:
            print(f"Error: No student with ID {student_id}.")
            return
        student = self.students[student_id]
        print(f"{student}:")
        for grade_item, grade in student.grades.items():
            total_points = self.grade_items[grade_item].total_points
            print(f"{grade_item}: {grade} / {total_points}")
    def print_roster(self):
        if not self.students:
            print("Error: Course Roster is Empty!")
            return
        print("Course Roster:")
        for student in self.students.values():
            print(student)
    def print_class_grades(self):
        if not self.students:
            print("Error: Course Roster is Empty!")
            return
        print("Class Grades:")
        for student in self.students.values():
            print(f"{student}:")
            for grade_item_name, grade_item in self.grade_items.items():
                grade = student.grades.get(grade_item_name, "N/A")
                print(f"  {grade_item_name}: {grade} / {grade_item.total_points}")
class EmptyRosterError(Exception):
    pass
def main():
    course = Course()
    print("Welcome to CSC/DSCI 1301: Principles in CS/DS 1")
    print("Please choose one of the following options (Enter 'quit' or 'q' to exit).")
    print("1) Add a Student.")
    print("2) Add a Grade Item.")
    print("3) Add a Student's Grade.")
    print("4) Print a Student's Grades.")
    print("5) Print Course Roster.")
    print("6) Print Class Grades.")
    print()
    while True:
        user_input = input(":> ").strip().lower()
        if user_input in ["quit", "q"]:
            print("Exiting the program. Goodbye!")
            break
        try:
            if user_input == "1":
                first_name = input("Enter First Name: ").strip()
                last_name = input("Enter Last Name: ").strip()
                while True:
                    try:
                        student_id = int(input("Enter Student ID: "))
                        break
                    except ValueError:
                        print("Error: Enter a valid Integer for Student ID.")
                student = Student(first_name, last_name, student_id)
                course.add_student(student)
            elif user_input == "2":
                grade_item_name = input("Enter grade item name: ").strip()
                while True:
                    try:
                        total_points = int(input("Enter the total points for the grade item: "))
                        break
                    except ValueError:
                        print("Error: Enter a valid Integer for total points.")
                grade_item = GradeItem(grade_item_name, total_points)
                course.add_grade_item(grade_item)
            elif user_input == "3":
                grade_item_name = input("Enter grade item name: ").strip()
                while True:
                    try:
                        student_id = int(input("Enter Student ID: "))
                        break
                    except ValueError:
                        print("Error: Enter a valid Integer for Student ID.")
                while True:
                    try:
                        grade = int(input("Enter Student Grade: "))
                        break
                    except ValueError:
                        print("Error: Enter a valid Integer for Student Grade.")
                course.add_student_grade(grade_item_name, student_id, grade)
            elif user_input == "4":
                while True:
                    try:
                        student_id = int(input("Enter Student ID: "))
                        break
                    except ValueError:
                        print("Error: Enter a valid Integer for Student ID.")
                course.print_student_grades(student_id)
            elif user_input == "5":
                try:
                    course.print_roster()
                except EmptyRosterError as e:
                    print(e)
            elif user_input == "6":
                try:
                    course.print_class_grades()
                except EmptyRosterError as e:
                    print(e)
            else:
                print("Error: Invalid option. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()
