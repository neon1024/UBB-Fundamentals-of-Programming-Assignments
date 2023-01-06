class Grade:

    def __init__(self, discipline_id: int, student_id: int, grade_value: int):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__grade_value = grade_value

        self.__all_grades = []

    def get_grade_value(self):
        return self.__grade_value

    def set_grade_value(self, new_grade_value: int):
        self.__grade_value = new_grade_value

    def get_discipline_id(self):
        return self.__discipline_id

    def set_discipline_id(self, new_discipline_id):
        self.__discipline_id = new_discipline_id

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, new_student_id):
        self.__student_id = new_student_id

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Discipline Id: {self.__discipline_id}, Student Id: {self.__student_id}, Grade Value: {self.__grade_value}"
