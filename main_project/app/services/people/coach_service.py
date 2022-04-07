from app.services.people.person_service import PersonService


class CoachService(PersonService):
    """
    class that extends the person server business logic for coach models.
    """

    def __init__(self, model, schemas) -> None:
        PersonService.__init__(self, model, schemas)

