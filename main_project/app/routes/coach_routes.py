from flask import Blueprint, request, Response
from app.models.people.coach_model import Coach
from app.routes.main_routes import minimum_request_bytes, resource_not_found
from app.schemas.people.coach_schema import CoachSchema
from app.services.people.coach_service import CoachService
from typing import Union, Dict, Any, List, Type


# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]
# Initialize the blueprint
coach_routes: Blueprint = Blueprint("coach_routes", __name__)
# Initialize the coach server:
coach_service: CoachService = CoachService(Coach, [CoachSchema(), CoachSchema(many=True)])


# coaches routes
@coach_routes.route('/coaches', methods=['GET', 'POST'])
def coaches() -> JSON:

    if request.method == 'GET':
        result = coach_service.get_items()
        if result.content_length < minimum_request_bytes:
            return resource_not_found
        return result

    if request.method == 'POST':
        return coach_service.add_item()


# coach id routes.
@coach_routes.route('/coaches/<int:coach_id>', methods=['GET', 'PUT', 'DELETE'])
def coach(coach_id) -> JSON:

    if not coach_service.get_item_by_id(coach_id):
        return resource_not_found

    if request.method == 'GET':
        return coach_service.get_item_by_id(coach_id)

    if request.method == 'PUT':
        return coach_service.update_item_by_id(coach_id)

    if request.method == 'DELETE':
        return coach_service.delete_item_by_id(coach_id)


# coach search route:
@coach_routes.route('/coaches/search', methods=['GET'])
def coach_search() -> JSON:
    result = coach_service.search_items()
    if result.content_length < minimum_request_bytes:
        return resource_not_found
    return result
