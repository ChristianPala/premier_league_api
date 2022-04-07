from flask import Blueprint, request, Response
from app.models.people.referee_model import Referee
from app.routes.main_routes import minimum_request_bytes, resource_not_found
from app.schemas.people.referee_schema import RefereeSchema
from app.services.people.referee_service import RefereeService
from typing import Union, Dict, Any, List, Type

# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]
# Initialize the blueprint
referee_routes: Blueprint = Blueprint("referee_routes", __name__)
# Initialize the referee server:
referee_service: RefereeService = RefereeService(Referee, [RefereeSchema(), RefereeSchema(many=True)])


# referees routes
@referee_routes.route('/referees', methods=['GET', 'POST'])
def referees() -> JSON:

    if request.method == 'GET':
        result = referee_service.get_items()

        if result.content_length < minimum_request_bytes:
            return resource_not_found
        return result

    if request.method == 'POST':
        return referee_service.add_item()


# referee id routes.
@referee_routes.route('/referees/<int:referee_id>', methods=['GET', 'PUT', 'DELETE'])
def referee(referee_id) -> JSON:

    if not referee_service.get_item_by_id(referee_id):
        return resource_not_found

    if request.method == 'GET':
        return referee_service.get_item_by_id(referee_id)

    if request.method == 'PUT':
        return referee_service.update_item_by_id(referee_id)

    if request.method == 'DELETE':
        return referee_service.delete_item_by_id(referee_id)


# search referees by query:
@referee_routes.route('/referees/search', methods=['GET'])
def referee_search() -> JSON:
    result = referee_service.search_items()
    if result.content_length < minimum_request_bytes:
        return resource_not_found
    return result

