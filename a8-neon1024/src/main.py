from src.repository.discipline_repository import DisciplinesRepository
from src.repository.grade_repository import GradesRepository
from src.repository.student_repository import StudentsRepository
from src.service.discipline_service import DisciplinesService
from src.service.grade_service import GradesService
from src.service.student_service import StudentsService
from src.ui.console import Console


def main():

    students_repository = StudentsRepository()
    students_service = StudentsService(students_repository)

    disciplines_repository = DisciplinesRepository()
    disciplines_service = DisciplinesService(disciplines_repository)

    grades_repository = GradesRepository()
    grades_service = GradesService(grades_repository)

    console = Console(students_service, disciplines_service, grades_service)
    console.run_console()


if __name__ == "__main__":

    main()
