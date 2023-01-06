import unittest

from src.repository.discipline_repository import DisciplinesRepository
from src.service.discipline_service import DisciplinesService


class TestStudentsService(unittest.TestCase):

    def setUp(self) -> None:

        self.__disciplines_repository = DisciplinesRepository()
        self.__disciplines_service = DisciplinesService(self.__disciplines_repository)

    def tearDown(self) -> None:

        del self.__disciplines_repository
        del self.__disciplines_service

    def test_add_discipline(self):
        self.__disciplines_service.add_discipline(1, "foo")

        all_disciplines = self.__disciplines_service.get_all_disciplines()

        self.assertEqual(all_disciplines[-1].get_id(), 1)
        self.assertEqual(all_disciplines[-1].get_name(), "foo")

    def test_remove_discipline(self):
        all_disciplines = list(self.__disciplines_service.get_all_disciplines())

        initial_length = len(all_disciplines)

        self.__disciplines_service.add_discipline(1, "foo")

        self.__disciplines_service.remove_discipline(1)

        all_disciplines = list(self.__disciplines_service.get_all_disciplines())

        self.assertEqual(initial_length, len(all_disciplines))

    def test_update_discipline(self):
        self.__disciplines_service.add_discipline(1, "foo")

        self.__disciplines_service.update_discipline(1, 2, "woo")

        all_disciplines = list(self.__disciplines_service.get_all_disciplines())

        self.assertEqual(all_disciplines[-1].get_id(), 2)
        self.assertEqual(all_disciplines[-1].get_name(), "woo")

    def test_search_disciplines_by_id(self):
        self.__disciplines_service.add_discipline(1, "foo")

        target_disciplines = self.__disciplines_service.search_disciplines_by_id(1)

        self.assertEqual(target_disciplines[-1].get_id(), 1)
        self.assertEqual(target_disciplines[-1].get_name(), "foo")

    def test_search_disciplines_by_name(self):
        self.__disciplines_service.add_discipline(1, "Foo")

        target_disciplines = self.__disciplines_service.search_disciplines_by_name("Foo".lower())

        self.assertEqual(target_disciplines[-1].get_id(), 1)
        self.assertEqual(target_disciplines[-1].get_name(), "Foo")

    def test_get_all_disciplines(self):
        self.__disciplines_service.add_discipline(1, "foo")

        all_disciplines = list(self.__disciplines_service.get_all_disciplines())

        self.assertEqual(all_disciplines[-1].get_id(), 1)
        self.assertEqual(all_disciplines[-1].get_name(), "foo")
