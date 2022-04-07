from app.services.people.person_service import PersonService


class RefereeService(PersonService):
    """
    class that extends the person server business logic for referee models.
    """

    def __init__(self, model, schemas) -> None:
        PersonService.__init__(self, model, schemas)
