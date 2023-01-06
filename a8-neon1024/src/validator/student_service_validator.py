class StudentsServiceValidator:

    @staticmethod
    def validate_existence(all_students, student_id):
        for student in all_students:
            if student.get_id() == student_id:
                return True
        return False

    @staticmethod
    def validate_uniqueness(all_students, student_id):
        for student in all_students:
            if student.get_id() == student_id:
                return False
        return True
