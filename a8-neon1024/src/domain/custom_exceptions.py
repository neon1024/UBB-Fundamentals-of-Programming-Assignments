class IdAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__("[!] Id already exists")


class IdDoesNotExistsError(Exception):
    def __init__(self):
        super().__init__("[!] Id doesn't exists")


class NameDoesNotExistsError(Exception):
    def __init__(self):
        super().__init__("[!] Name doesn't exists")


class DuplicatedGradesError(Exception):
    def __init__(self):
        super().__init__("[!] Duplicated grades")


class InvalidInputError(Exception):
    def __init__(self):
        super().__init__("[!] Invalid input")
