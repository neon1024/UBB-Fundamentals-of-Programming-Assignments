from src.domain.custom_exceptions import DuplicatedGradesError, IdDoesNotExistsError, IdAlreadyExistsError
from src.domain.grade import Grade
from src.validator.grade_service_validator import GradesServiceValidator


class GradesService:

    def __init__(self, grades_repository):
        self.__grade_repository = grades_repository
        self.__grades_service_validator = GradesServiceValidator()
        self.__undo_list = [self.__grade_repository.get_all_grades()]

    def grade_student(self, discipline_id, student_id, grade_values):
        OLD_LIST = -1   # index of the last list of undo_list

        all_grades = list(self.__grade_repository.get_all_grades())

        if self.__grades_service_validator.validate_grade_uniqueness(all_grades, discipline_id, student_id, grade_values):

            for grade_value in grade_values:
                grade = Grade(discipline_id, student_id, grade_value)
                all_grades.append(grade)

            if all_grades != self.__undo_list[OLD_LIST]:
                self.__grade_repository.save(all_grades)
                self.__undo_list.append(all_grades)

        else:
            raise DuplicatedGradesError()

    def remove_student(self, removing_id):
        OLD_LIST = -1  # index of the last list of undo_list

        all_grades = self.__grade_repository.get_all_grades()

        if self.__grades_service_validator.validate_student_existence(all_grades, removing_id):

            index = 0

            while index < len(all_grades):
                if all_grades[index].get_student_id() == removing_id:
                    all_grades.pop(index)
                else:
                    index += 1

            if all_grades != self.__undo_list[OLD_LIST]:
                self.__grade_repository.save(all_grades)
                self.__undo_list.append(all_grades)

        else:
            raise IdDoesNotExistsError()

    def update_student(self, updating_id, new_student_id):
        OLD_LIST = -1  # index of the last list of undo_list

        all_grades = list(self.__grade_repository.get_all_grades())

        if self.__grades_service_validator.validate_student_existence(all_grades, updating_id):
            if self.__grades_service_validator.validate_student_uniqueness(all_grades, new_student_id):

                index = 0

                while index < len(all_grades):
                    if all_grades[index].get_student_id() == updating_id:
                        all_grades[index].set_student_id(new_student_id)

                    index += 1

                if all_grades != self.__undo_list[OLD_LIST]:
                    self.__grade_repository.save(all_grades)
                    self.__undo_list.append(all_grades)

            else:
                raise IdAlreadyExistsError()
        else:
            raise IdDoesNotExistsError()

    def remove_discipline(self, removing_id):
        OLD_LIST = -1  # index of the last list of undo_list

        all_grades = self.__grade_repository.get_all_grades()

        if self.__grades_service_validator.validate_discipline_existence(all_grades, removing_id):

            index = 0

            while index < len(all_grades):
                if all_grades[index].get_discipline_id() == removing_id:
                    all_grades.pop(index)
                else:
                    index += 1

            if all_grades != self.__undo_list[OLD_LIST]:
                self.__grade_repository.save(all_grades)
                self.__undo_list.append(all_grades)

        else:
            raise IdDoesNotExistsError()

    def update_discipline(self, updating_id, new_discipline_id):
        OLD_LIST = -1   # index of the last list of undo_list

        all_grades = self.__grade_repository.get_all_grades()

        if self.__grades_service_validator.validate_discipline_existence(all_grades, updating_id):

            index = 0

            while index < len(all_grades):
                if all_grades[index].get_discipline_id() == updating_id:
                    all_grades[index].set_discipline_id(new_discipline_id)

                index += 1

            if all_grades != self.__undo_list[OLD_LIST]:
                self.__grade_repository.save(all_grades)
                self.__undo_list.append(all_grades)

        else:
            raise IdDoesNotExistsError()

    def get_all_grades(self):
        return self.__grade_repository.get_all_grades()

    def get_failing_students(self, all_students, all_disciplines):
        failing_students = []

        for student in all_students:
            student_id = student.get_id()

            for discipline in all_disciplines:
                discipline_id = discipline.get_id()
                sum_of_grades = 0
                number_of_grades = 0

                all_grades = list(self.__grade_repository.get_all_grades())
                for grade in all_grades:
                    if grade.get_student_id() == student_id and grade.get_discipline_id() == discipline_id:
                        sum_of_grades += grade.get_grade_value()
                        number_of_grades += 1

                if number_of_grades != 0:
                    average_grade = sum_of_grades/number_of_grades

                    if average_grade < 5:
                        failing_students.append(student)
                        break

        return failing_students

    def get_best_students_in_descending_order(self, all_students, all_disciplines):
        students_aggregated_averages = []

        for student in all_students:
            student_id = student.get_id()
            sum_of_disciplines_average_grades = 0
            number_of_disciplines = 0

            for discipline in all_disciplines:
                discipline_id = discipline.get_id()
                sum_of_grades = 0
                number_of_grades = 0

                all_grades = list(self.__grade_repository.get_all_grades())
                for grade in all_grades:
                    if grade.get_student_id() == student_id and grade.get_discipline_id() == discipline_id:
                        sum_of_grades += grade.get_grade_value()
                        number_of_grades += 1

                if number_of_grades != 0:
                    average_grade = sum_of_grades/number_of_grades
                    sum_of_disciplines_average_grades += average_grade
                    number_of_disciplines += 1

            if number_of_disciplines != 0:
                aggregated_average = sum_of_disciplines_average_grades/number_of_disciplines
                students_aggregated_averages.append({"Student Id": student_id, "Student Name": student.get_name(), "Aggregated Average": aggregated_average})

        for i in range(0, len(students_aggregated_averages)-1):
            if students_aggregated_averages[i]["Aggregated Average"] < students_aggregated_averages[i+1]["Aggregated Average"]:
                students_aggregated_averages[i], students_aggregated_averages[i+1] = students_aggregated_averages[i+1], students_aggregated_averages[i]

        ok = True

        while ok:

            ok = False

            for i in range(0, len(students_aggregated_averages) - 1):
                if students_aggregated_averages[i]["Aggregated Average"] < students_aggregated_averages[i + 1]["Aggregated Average"]:
                    students_aggregated_averages[i], students_aggregated_averages[i + 1] = students_aggregated_averages[i + 1], students_aggregated_averages[i]
                    ok = True

        return students_aggregated_averages

    def get_all_disciplines_with_at_least_one_grade_in_descending_order(self, all_disciplines, all_students):
        disciplines_with_at_least_one_grade = []

        for discipline in all_disciplines:
            discipline_id = discipline.get_id()
            sum_of_average_grades_of_all_students = 0
            number_of_students = 0

            for student in all_students:
                student_id = student.get_id()
                sum_of_grades = 0
                number_of_grades = 0

                all_grades = list(self.__grade_repository.get_all_grades())
                for grade in all_grades:
                    if grade.get_student_id() == student_id and grade.get_discipline_id() == discipline_id:
                        sum_of_grades += grade.get_grade_value()
                        number_of_grades += 1

                if number_of_grades != 0:
                    average_grade = sum_of_grades/number_of_grades
                    sum_of_average_grades_of_all_students += average_grade
                    number_of_students += 1

            if number_of_students != 0:
                average_grade_of_discipline = sum_of_average_grades_of_all_students/number_of_students
                disciplines_with_at_least_one_grade.append({"Discipline Id": discipline_id, "Average Grade": average_grade_of_discipline})

        for i in range(0, len(disciplines_with_at_least_one_grade)-1):
            if disciplines_with_at_least_one_grade[i]["Average Grade"] < disciplines_with_at_least_one_grade[i+1]["Average Grade"]:
                disciplines_with_at_least_one_grade[i], disciplines_with_at_least_one_grade[i+1] = disciplines_with_at_least_one_grade[i+1], disciplines_with_at_least_one_grade[i]

        ok = True

        while ok:

            ok = False

            for i in range(0, len(disciplines_with_at_least_one_grade) - 1):
                if disciplines_with_at_least_one_grade[i]["Average Grade"] < disciplines_with_at_least_one_grade[i + 1]["Average Grade"]:
                    disciplines_with_at_least_one_grade[i], disciplines_with_at_least_one_grade[i + 1] = disciplines_with_at_least_one_grade[i + 1], disciplines_with_at_least_one_grade[i]
                    ok = True

        return disciplines_with_at_least_one_grade
