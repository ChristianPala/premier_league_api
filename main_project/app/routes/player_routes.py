from flask import Blueprint, request, Response
from app.models.people.player_model import Player
from app.routes.main_routes import minimum_request_bytes, resource_not_found
from app.schemas.people.player_schema import PlayerSchema
from app.services.people.player_service import PlayerService
from typing import Union, Dict, Any, List, Type

# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]
# Initialize the blueprint
player_routes: Blueprint = Blueprint("player_routes", __name__)
# Initialize the player server:
player_service: PlayerService = PlayerService(Player, [PlayerSchema(), PlayerSchema(many=True)])


# players routes
@player_routes.route('/players', methods=['GET', 'POST'])
def players() -> JSON:

    if request.method == 'GET':

        result = player_service.get_items()

        if result.content_length < minimum_request_bytes:
            return resource_not_found
        return result

    if request.method == 'POST':
        return player_service.add_item()


# player id routes.
@player_routes.route('/players/<int:player_id>', methods=['GET', 'PUT', 'DELETE'])
def player(player_id) -> JSON:

    if not player_service.get_item_by_id(player_id):
        return resource_not_found

    if request.method == 'GET':
        return player_service.get_item_by_id(player_id)

    if request.method == 'PUT':
        return player_service.update_item_by_id(player_id)

    if request.method == 'DELETE':
        return player_service.delete_item_by_id(player_id)


# search players by query:
@player_routes.route('/players/search', methods=['GET'])
def player_search() -> JSON:
    result = player_service.search_items()

    if result.content_length < minimum_request_bytes:
        return resource_not_found
    return result
