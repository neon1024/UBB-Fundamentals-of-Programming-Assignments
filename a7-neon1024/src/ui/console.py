class Console:

    def __init__(self, students_service):

        self.students_service = students_service

        self.console_options = {
            "1": self.add_a_student,
            "2": self.show_all_students,
            "3": self.delete_students_by_group,
            "4": self.undo,
            "x": self.exit_program
        }

    def add_a_student(self):

        student_id = int(input("Id: "))
        student_name = input("Name: ")
        student_group = int(input("Group: "))

        self.students_service.add_student(student_id, student_name, student_group)

    def show_all_students(self):
        all_students = self.students_service.get_all_students()

        for student in all_students:
            print(student)

    def delete_students_by_group(self):
        group = int(input("Group: "))

        self.students_service.delete_students_by_group(group)

    def undo(self):
        self.students_service.undo()

    @staticmethod
    def exit_program():
        exit()

    def run_console(self):
        while True:
            try:

                self.print_console_options()

                chosen_option = input("> ")

                self.console_options[chosen_option]()

            except Exception as error:
                print(str(error))

    @staticmethod
    def print_console_options():

        print("1: Add a student. Student data is read from the console.")
        print("2: Display the list of students")
        print("3: Filter the list so that students in a given group (read from the console) are deleted from the list.")
        print("4: Undo the last operation that modified program data. This step can be repeated. The user can undo only those operations made during the current run of the program.")
        print("x: Exit")
