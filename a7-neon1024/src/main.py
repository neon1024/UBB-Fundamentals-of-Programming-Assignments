from src.repository.students_repository import StudentsMemoryRepository, StudentsTextFileRepository, StudentsBinaryFileRepository, StudentsJSONFileRepository
from src.services.students_service import StudentsService
from src.ui.console import Console
from jproperties import Properties


def main():

    config = Properties()

    with open("settings/settings.properties", "rb") as settings:
        config.load(settings)

    chosen_repository = config.get("StudentsRepository")
    chosen_repository = str(chosen_repository.data)

    students_repositories = {
        "StudentsMemoryRepository": StudentsMemoryRepository,
        "StudentsTextFileRepository": StudentsTextFileRepository,
        "StudentsBinaryFileRepository": StudentsBinaryFileRepository,
        "StudentsJSONFileRepository": StudentsJSONFileRepository
    }

    students_repository = students_repositories[chosen_repository]()
    students_service = StudentsService(students_repository)
    console = Console(students_service)
    console.run_console()


if __name__ == "__main__":

    main()
