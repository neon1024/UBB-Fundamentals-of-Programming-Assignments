import unittest
from src.services.students_service import StudentsService
from src.repository.students_repository import StudentsMemoryRepository
from src.domain.students import Student


class TestService(unittest.TestCase):

    def setUp(self):

        self.students_repository = StudentsMemoryRepository()
        self.students_service = StudentsService(self.students_repository)

    def tearDown(self):

        del self.students_service
        del self.students_repository

    def test_add_student(self):

        student_id = 1
        student_name = "John Snow"
        student_group = 2

        student = Student(student_id, student_name, student_group)

        self.students_service.add_student(student_id, student_name, student_group)

        all_students = self.students_repository.get_all_students()
        last_added_student = all_students[-1]

        self.assertEqual(last_added_student.get_id(), student.get_id())
        self.assertEqual(last_added_student.get_name(), student.get_name())
        self.assertEqual(last_added_student.get_group(), student.get_group())

    def test_delete_students_by_group(self):

        all_students = self.students_repository.get_all_students()

        initial_length_of_the_list = len(all_students)

        student_id = 1
        student_name = "John Snow"
        student_group = 2

        self.students_service.add_student(student_id, student_name, student_group)

        self.students_service.delete_students_by_group(student_group)

        self.assertEqual(initial_length_of_the_list, len(self.students_repository.get_all_students()))

    def test_undo(self):
        all_students = self.students_repository.get_all_students()

        initial_length_of_the_list = len(all_students)

        student_id = 1
        student_name = "John Snow"
        student_group = 2

        self.students_service.add_student(student_id, student_name, student_group)

        self.students_service.undo()

        self.assertEqual(initial_length_of_the_list, len(self.students_repository.get_all_students()))
