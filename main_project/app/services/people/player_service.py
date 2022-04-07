from app.services.people.person_service import PersonService


class PlayerService(PersonService):
    """
    class that extends the person server business logic for player models.
    """
    def __init__(self, model, schemas) -> None:
        PersonService.__init__(self, model, schemas)
