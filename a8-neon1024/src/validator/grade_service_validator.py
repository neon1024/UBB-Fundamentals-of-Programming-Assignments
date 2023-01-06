class GradesServiceValidator:

    @staticmethod
    def validate_discipline_existence(all_grades, discipline_id):
        for grade in all_grades:
            if grade.get_discipline_id() == discipline_id:
                return True
        return False

    @staticmethod
    def validate_discipline_uniqueness(all_grades, discipline_id):
        for grade in all_grades:
            if grade.get_discipline_id() == discipline_id:
                return False
        return True

    @staticmethod
    def validate_student_existence(all_grades, student_id):
        for grade in all_grades:
            if grade.get_student_id() == student_id:
                return True
        return False

    @staticmethod
    def validate_student_uniqueness(all_grades, student_id):
        for grade in all_grades:
            if grade.get_student_id() == student_id:
                return False
        return True

    @staticmethod
    def validate_grade_existence(all_grades, discipline_id, student_id, grade_values):
        for grade in all_grades:
            if grade.get_student_id() == student_id and grade.get_discipline_id() == discipline_id and grade.get_grade_value() in grade_values:
                return True
        return False

    @staticmethod
    def validate_grade_uniqueness(all_grades, discipline_id, student_id, grade_values):
        for grade in all_grades:
            if grade.get_student_id() == student_id and grade.get_discipline_id() == discipline_id and grade.get_grade_value() in grade_values:
                return False
        return True
