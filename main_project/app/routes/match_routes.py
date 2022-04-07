from flask import Blueprint, request
from app.models.match_model import Match
from app.routes.main_routes import minimum_request_bytes, resource_not_found
from app.schemas.match_schema import MatchSchema
from app.services.match_service import MatchService
from typing import Union, Dict, Any, List, Type

# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]
# Initialize the blueprint
match_routes: Blueprint = Blueprint("match_routes", __name__)
# Initialize the match server:
match_service: MatchService = MatchService(Match, [MatchSchema(), MatchSchema(many=True)])


# matches routes
@match_routes.route('/matches', methods=['GET', 'POST'])
def matches() -> JSON:

    if request.method == 'GET':
        result = match_service.get_items()
        if result.content_length < minimum_request_bytes:
            return resource_not_found
        return match_service.get_items()

    if request.method == 'POST':
        return match_service.add_item()


# match id routes.
@match_routes.route('/matches/<int:match_id>', methods=['GET', 'PUT', 'DELETE'])
def match(match_id) -> JSON:

    if not match_service.get_item_by_id(match_id):
        return resource_not_found

    if request.method == 'GET':
        return match_service.get_item_by_id(match_id)

    if request.method == 'PUT':
        return match_service.update_item_by_id(match_id)

    if request.method == 'DELETE':
        return match_service.delete_item_by_id(match_id)


# search matches by query:
@match_routes.route('/matches/search', methods=['GET'])
def match_search() -> JSON:
    result = match_service.search_items()
    if result.content_length < minimum_request_bytes:
        return resource_not_found
    return match_service.search_items()
