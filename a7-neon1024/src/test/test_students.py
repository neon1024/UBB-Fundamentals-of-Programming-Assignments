import unittest

from src.domain.students import Student


class TestStudent(unittest.TestCase):

    def setUp(self):

        self.student = Student(1, "Steve", 101)

    def tearDown(self):

        del self.student

    def test_init(self):

        self.assertEqual(self.student.get_id(), 1)
        self.assertEqual(self.student.get_name(), "Steve")
        self.assertEqual(self.student.get_group(), 101)

    def test_set_id(self):

        self.student.set_id(202)
        self.assertEqual(self.student.get_id(), 202)

    def test_set_name(self):

        self.student.set_name("Alex")
        self.assertEqual(self.student.get_name(), "Alex")

    def test_set_group(self):

        self.student.set_group(1000)
        self.assertEqual(self.student.get_group(), 1000)

    def test_repr(self):

        self.assertEqual(str(self.student), repr(self.student))

    def test_str(self):

        student_as_string = str(self.student)
        self.assertEqual(student_as_string, f"Id: {self.student.get_id()}, Name: {self.student.get_name()}, Group: {self.student.get_group()}")
