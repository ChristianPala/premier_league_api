from app.services.base_service import BaseService
from typing import Dict, Any, List, Type, Union


# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class PersonService(BaseService):
    # abstract class extending the base business logic for a person model.
    def __init__(self, model, schemas) -> None:
        """
        constructor for a server of type person. remember to insert the single schema first in the
        list of schemas.
        """
        BaseService.__init__(self, model, schemas)
