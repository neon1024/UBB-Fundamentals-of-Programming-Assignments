from src.domain.students import Student
import random
from pathlib import Path
import pickle
import json


class StudentsMemoryRepository:

    def __init__(self):
        self.__all_students = self.generate_random_students(10)

    @staticmethod
    def generate_random_students(number_of_random_students_to_generate: int):
        first_names = ["Alex", "John", "Steve", "Stacy", "Alexa"]
        last_names = ["Johnson", "Peterson", "Harley", "Smith", "Williams"]

        random_generated_students = []

        for index in range(0, number_of_random_students_to_generate):
            random_student_id = random.randint(100, 999)
            random_student_name = random.choice(first_names) + " " + random.choice(last_names)
            random_student_group = random.randint(911, 917)

            random_student = Student(random_student_id, random_student_name, random_student_group)

            random_generated_students.append(random_student)

        return random_generated_students

    def get_all_students(self):
        return self.__all_students

    def save_students(self, list_of_students):
            self.__all_students = list_of_students


class StudentsTextFileRepository:

    def __init__(self):

        self.__all_students = []

        students_file = Path("data/students.txt")

        if students_file.is_file():
            # load students from existing file
            self.__all_students = self.load_students()

        else:
            # generate random students
            self.__all_students = self.generate_random_students(10)

        self.save_students(self.__all_students) # we save them in order to write in file even if we don't perform tasks

    def save_students(self, list_of_students):

        self.__all_students = list_of_students

        with open("data/students.txt", "w") as file:  # with automatically closes the files

            for student in list_of_students:
                student_id = student.get_id()
                student_name = student.get_name()
                student_group = student.get_group()

                file.write("%s %s %s\n" % (student_id, student_name, student_group))

    @staticmethod
    def load_students():

        ID = 0  # position of the id in line_elements array
        FIRST_NAME = 1  # position of the first_name in line_elements array
        LAST_NAME = 2  # position of the last_name in line_elements array
        GROUP = 3  # position of the group in line_elements array

        loaded_students = []

        with open("data/students.txt", "r") as file:  # with automatically closes the files

            for line in file:
                line_elements = line.split(" ")

                student_id = int(line_elements[ID])
                student_name = line_elements[FIRST_NAME] + " " + line_elements[LAST_NAME]
                student_group = int(line_elements[GROUP])

                student = Student(student_id, student_name, student_group)

                loaded_students.append(student)

        return loaded_students

    @staticmethod
    def generate_random_students(number_of_random_students_to_generate: int):
        first_names = ["Alex", "John", "Steve", "Stacy", "Alexa"]
        last_names = ["Johnson", "Peterson", "Harley", "Smith", "Williams"]

        random_generated_students = []

        for index in range(0, number_of_random_students_to_generate):
            random_student_id = random.randint(100, 999)
            random_student_name = random.choice(first_names) + " " + random.choice(last_names)
            random_student_group = random.randint(911, 917)

            random_student = Student(random_student_id, random_student_name, random_student_group)

            random_generated_students.append(random_student)

        return random_generated_students

    def get_all_students(self):
        return self.__all_students


class StudentsBinaryFileRepository:

    def __init__(self):
        self.__all_students = []
        students_file = Path("data/students")
        if students_file.is_file():
            # load students from existing file
            self.__all_students = self.load_students()
        else:
            # generate random students
            self.__all_students = self.generate_random_students(10)
        self.save_students(self.__all_students)

    def save_students(self, list_of_students):
        self.__all_students = list_of_students
        with open("data/students", "wb") as file:  # with automatically closes the files
            pickle.dump(list_of_students, file)

    @staticmethod
    def load_students():
        with open("data/students", "rb") as file:  # with automatically closes the files
            loaded_students = pickle.load(file)
        return loaded_students

    @staticmethod
    def generate_random_students(number_of_random_students_to_generate: int):
        first_names = ["Alex", "John", "Steve", "Stacy", "Alexa"]
        last_names = ["Johnson", "Peterson", "Harley", "Smith", "Williams"]

        random_generated_students = []

        for index in range(0, number_of_random_students_to_generate):
            random_student_id = random.randint(100, 999)
            random_student_name = random.choice(first_names) + " " + random.choice(last_names)
            random_student_group = random.randint(911, 917)

            random_student = Student(random_student_id, random_student_name, random_student_group)

            random_generated_students.append(random_student)

        return random_generated_students

    def get_all_students(self):
        return self.__all_students


class StudentsJSONFileRepository:

    def __init__(self):
        self.__all_students = []
        students_file = Path("data/students.json")
        if students_file.is_file():
            # load students from existing file
            self.__all_students = self.load_students()
        else:
            # generate random students
            self.__all_students = self.generate_random_students(10)
        self.save_students(self.__all_students)

    def save_students(self, list_of_students):
        self.__all_students = list_of_students
        list_of_students_as_dictionaries = []
        for student in list_of_students:
            student_id = student.get_id()
            student_name = student.get_name()
            student_group = student.get_group()
            student_as_dictionary = {"id": student_id, "name": student_name, "group": student_group}
            list_of_students_as_dictionaries.append(student_as_dictionary)
        jsonString = json.dumps(list_of_students_as_dictionaries)
        with open("data/students.json", "w") as file:
            jsonFile = file
            jsonFile.write(jsonString)

    @staticmethod
    def load_students():
        loaded_students = []
        with open("data/students.json", "r") as file:  # with automatically closes the files
            jsonString = file.read()
            list_of_students_as_dictionaries = json.loads(jsonString)
            for student_as_dictionary in list_of_students_as_dictionaries:
                student_id = student_as_dictionary["id"]
                student_name = student_as_dictionary["name"]
                student_group = student_as_dictionary["group"]
                student = Student(student_id, student_name, student_group)
                loaded_students.append(student)
        return loaded_students

    @staticmethod
    def generate_random_students(number_of_random_students_to_generate: int):
        first_names = ["Alex", "John", "Steve", "Stacy", "Alexa"]
        last_names = ["Johnson", "Peterson", "Harley", "Smith", "Williams"]

        random_generated_students = []

        for index in range(0, number_of_random_students_to_generate):
            random_student_id = random.randint(100, 999)
            random_student_name = random.choice(first_names) + " " + random.choice(last_names)
            random_student_group = random.randint(911, 917)

            random_student = Student(random_student_id, random_student_name, random_student_group)

            random_generated_students.append(random_student)

        return random_generated_students

    def get_all_students(self):
        return self.__all_students
