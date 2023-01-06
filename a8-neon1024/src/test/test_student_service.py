import unittest

from src.repository.student_repository import StudentsRepository
from src.service.student_service import StudentsService


class TestStudentsService(unittest.TestCase):

    def setUp(self) -> None:

        self.__students_repository = StudentsRepository()
        self.__students_service = StudentsService(self.__students_repository)

    def tearDown(self) -> None:

        del self.__students_repository
        del self.__students_service

    def test_add_student(self):
        self.__students_service.add_student(11, "John Snow")

        all_students = self.__students_service.get_all_students()

        self.assertEqual(all_students[-1].get_id(), 11)
        self.assertEqual(all_students[-1].get_name(), "John Snow")

    def test_remove_student(self):
        all_students = list(self.__students_service.get_all_students())

        initial_length = len(all_students)

        self.__students_service.add_student(11, "John Snow")

        self.__students_service.remove_student(11)

        all_students = list(self.__students_service.get_all_students())

        self.assertEqual(initial_length, len(all_students))

    def test_update_student(self):
        self.__students_service.add_student(11, "John Snow")

        self.__students_service.update_student(11, 12, "John Ice")

        all_students = list(self.__students_service.get_all_students())

        self.assertEqual(all_students[-1].get_id(), 12)
        self.assertEqual(all_students[-1].get_name(), "John Ice")

    def test_search_students_by_id(self):
        self.__students_service.add_student(11, "John Snow")

        target_students = self.__students_service.search_students_by_id(11)

        self.assertEqual(target_students[-1].get_id(), 11)
        self.assertEqual(target_students[-1].get_name(), "John Snow")

    def test_search_students_by_name(self):
        self.__students_service.add_student(11, "John Snow")

        target_students = self.__students_service.search_students_by_name("John Snow".lower())

        self.assertEqual(target_students[-1].get_id(), 11)
        self.assertEqual(target_students[-1].get_name(), "John Snow")

    def test_get_all_students(self):
        self.__students_service.add_student(11, "John Snow")

        all_students = list(self.__students_service.get_all_students())

        self.assertEqual(all_students[-1].get_id(), 11)
        self.assertEqual(all_students[-1].get_name(), "John Snow")
