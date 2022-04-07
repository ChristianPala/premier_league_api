from pl_client.services.people.person_service import PersonService
from pl_client.models.people.player import Player
from pl_client.services.utils import string_to_date, date_to_string
from typing import List, Optional, Tuple, Union, Type, Any, Dict

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class PlayerService(PersonService):
    route_name = 'players'

    @classmethod
    def _write_query(cls, name=None, surname=None, nationality=None, birth_date=None, role=None, height=None) \
            -> Optional[str]:

        query = str()

        if name:
            query = f'name={name}'

        if surname:
            if not query:
                query = f'surname={surname}'
            else:
                query = f'{query}&surname={surname}'

        if birth_date:
            if not query:
                query = f'birth_date={birth_date}'
            else:
                query = f'{query}&birth_date={birth_date}'

        if nationality:
            if not query:
                query = f'nationality={nationality}'
            else:
                query = f'{query}&nationality={nationality}'

        if role:
            if not query:
                query = f'role={role}'
            else:
                query = f'{query}&role={role}'

        if height:
            if not query:
                query = f'height={height}'
            else:
                query = f'{query}&height={height}'

        return query

    @classmethod
    def _create_dict(cls, item_data: Any):
        model_dict = dict()
        if item_data.name:
            model_dict.update({"name": item_data.name})

        if item_data.surname:
            model_dict.update({"surname": item_data.surname})

        if item_data.birth_date:
            model_dict.update({"birth_date": date_to_string(item_data.birth_date)})

        if item_data.nationality:
            model_dict.update({"nationality": item_data.nationality})

        if item_data.role:
            model_dict.update({"role": item_data.role})

        if item_data.height:
            model_dict.update({"height": str(item_data.height) + " cm"})

        return model_dict

    def __init__(self) -> None:
        """
        Constructor for a player service.
        """
        PersonService.__init__(self, PlayerService.route_name)

    @classmethod
    def get_all(cls) -> List[Player]:
        """
            method to return all players in the database.
        """
        player_list: list = []
        player_res: dict = cls._get_items(cls.route_name)
        for item in player_res:
            player_list.append(Player(name=item['name'],
                                      role=item['role'],
                                      surname=item['surname'],
                                      birth_date=string_to_date(item['birth_date']),
                                      nationality=item['nationality'],
                                      height=item['height']))
        return player_list

    @classmethod
    def get_item_by_id(cls, player_id: int) -> Player:
        """
        method to fetch a player by id in the database.
        """
        player_res: dict = cls._get_item_by_id(player_id, cls.route_name)
        new_player = Player(name=player_res['name'],
                            surname=player_res['surname'],
                            birth_date=string_to_date(player_res['birth_date']),
                            nationality=player_res['nationality'],
                            role=player_res['role'],
                            height=int(player_res['height']))
        return new_player

    @classmethod
    def add_item(cls, item_to_add: Player) -> int:
        """
            method to add a player to the database.
        """
        player_dict = item_to_add.__dict__()
        response_status: int = cls._add_item(player_dict, cls.route_name)
        return response_status

    @classmethod
    def update_item_by_id(cls, item_id: int, item_data: Player) -> int:
        """
            method to update a player in the database.
        """
        player_dict: dict = cls._create_dict(item_data)

        response_status: int = cls._update_item_by_id(item_id, player_dict, cls.route_name)
        return response_status

    @classmethod
    def delete_item_by_id(cls, item_id: int) -> int:
        """
            method to delete a player in the database.
        """
        response_status: int = cls._delete_item_by_id(item_id, cls.route_name)
        return response_status

    @classmethod
    def search_items(cls, name=None, surname=None, birth_date=None, nationality=None,
                     role=None, height=None) -> Optional[List[Player]]:
        """
            method to search all players by their attributes in the database.
        """
        query: str = cls._write_query(name=name,
                                       surname=surname,
                                       birth_date=birth_date,
                                       nationality=nationality,
                                       role=role,
                                       height=height)

        player_list: list = []
        player_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)

        if player_res[1] != 404:
            for item in player_res[0]:
                player_list.append(Player(name=item['name'],
                                          role=item['role'],
                                          surname=item['surname'],
                                          birth_date=string_to_date(item['birth_date']),
                                          nationality=item['nationality'],
                                          height=item['height']))
        return player_list

    @classmethod
    def find_ids(cls, name=None, surname=None, birth_date=None, nationality=None,
                 role=None, height=None) -> List[Dict]:
        """
            return the id's of team objects in the database with the parameters requested by the user.
        """
        query: str = cls._write_query(name=name,
                                       surname=surname,
                                       birth_date=birth_date,
                                       nationality=nationality,
                                       role=role,
                                       height=height)

        team_list: list = []
        team_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if team_res[1] != 404:
            for item in team_res[0]:
                team_list.append({"id": item['id'],
                                  "name": item['name'],
                                  "surname": item['surname'],
                                  "role": item['role']})
        return team_list


