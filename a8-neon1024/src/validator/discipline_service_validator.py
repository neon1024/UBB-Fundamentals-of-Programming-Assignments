class DisciplinesServiceValidator:

    @staticmethod
    def validate_existence(all_disciplines, discipline_id):
        for discipline in all_disciplines:
            if discipline.get_id() == discipline_id:
                return True
        return False

    @staticmethod
    def validate_uniqueness(all_disciplines, discipline_id):
        for discipline in all_disciplines:
            if discipline.get_id() == discipline_id:
                return False
        return True
