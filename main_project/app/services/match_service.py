from app.services.base_service import BaseService


class MatchService(BaseService):
    """
    class that extends the base server logic for the match model.
    """

    def __init__(self, model, schemas) -> None:
        BaseService.__init__(self, model, schemas)
