from app.services.base_service import BaseService


class TeamService(BaseService):
    """
    class that extends the base server logic for the team model.
    """

    def __init__(self, model, schemas) -> None:
        BaseService.__init__(self, model, schemas)
