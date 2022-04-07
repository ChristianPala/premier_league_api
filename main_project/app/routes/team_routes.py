from flask import Blueprint, request
from app.models.team_model import Team
from app.routes.main_routes import minimum_request_bytes, resource_not_found
from app.schemas.team_schema import TeamSchema
from app.services.team_service import TeamService
from typing import Union, Dict, Any, List, Type

# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]
# Initialize the blueprint
team_routes: Blueprint = Blueprint("team_routes", __name__)
# Initialize the team server:
team_service: TeamService = TeamService(Team, [TeamSchema(), TeamSchema(many=True)])


# teams routes
@team_routes.route('/teams', methods=['GET', 'POST'])
def teams() -> JSON:

    if request.method == 'GET':
        result = team_service.get_items()
        if result.content_length < minimum_request_bytes:
            return resource_not_found
        return team_service.get_items()

    if request.method == 'POST':
        return team_service.add_item()


# team id routes.
@team_routes.route('/teams/<int:team_id>', methods=['GET', 'PUT', 'DELETE'])
def team(team_id) -> JSON:

    if not team_service.get_item_by_id(team_id):
        return resource_not_found

    if request.method == 'GET':
        return team_service.get_item_by_id(team_id)

    if request.method == 'PUT':
        return team_service.update_item_by_id(team_id)

    if request.method == 'DELETE':
        return team_service.delete_item_by_id(team_id)


# search teams by query:
@team_routes.route('/teams/search', methods=['GET'])
def team_search() -> JSON:
    result = team_service.search_items()
    if result.content_length < minimum_request_bytes:
        return resource_not_found
    return team_service.search_items()
