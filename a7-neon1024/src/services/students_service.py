from src.domain.students import Student


class StudentsService:

    def __init__(self, students_repository):
        self.students_repository = students_repository
        self.undo_list = [self.students_repository.get_all_students()]

    def add_student(self, student_id, student_name, student_group):
        LAST_GENERATED_LIST_OF_STUDENTS = -1  # The position of the last generated list of students

        student = Student(student_id, student_name, student_group)

        all_students = list(self.students_repository.get_all_students())

        all_students.append(student)

        if all_students != self.undo_list[LAST_GENERATED_LIST_OF_STUDENTS]:
            self.undo_list.append(all_students)
            self.students_repository.save_students(all_students)

    def get_all_students(self):
        return self.students_repository.get_all_students()

    def delete_students_by_group(self, deleting_group: int):
        LAST_GENERATED_LIST_OF_STUDENTS = -1  # The position of the last generated list of students

        all_students = list(self.students_repository.get_all_students())

        index = 0

        while index < len(all_students):
            if all_students[index].get_group() == deleting_group:
                all_students.pop(index)
            else:
                index += 1

        if all_students != self.undo_list[LAST_GENERATED_LIST_OF_STUDENTS]:
            self.undo_list.append(all_students)
            self.students_repository.save_students(all_students)

    def undo(self):
        LAST_GENERATED_LIST_OF_STUDENTS = -1  # The position of the last generated list of students

        if len(self.undo_list) > 1:
            self.undo_list.pop()
            self.students_repository.save_students(self.undo_list[LAST_GENERATED_LIST_OF_STUDENTS])
