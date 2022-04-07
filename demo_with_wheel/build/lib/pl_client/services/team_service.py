# Libraries:
from __future__ import annotations
from pl_client.services.base_service import BaseService
from pl_client.models.team import Team
from typing import Dict, Any, List, Type, Union, Optional, Tuple

# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class TeamService(BaseService):
    route_name = 'teams'

    @classmethod
    def _create_dict(cls, item_data: Any):
        model_dict = dict()
        if item_data.name:
            model_dict.update({"name": item_data.name})

        if item_data.address:
            model_dict.update({"address": item_data.address})

        if item_data.stadium:
            model_dict.update({"stadium": item_data.stadium})

        if item_data.url:
            model_dict.update({"url": item_data.url})

        return model_dict

    @classmethod
    def _write_query(cls, name=None, address=None, stadium=None, url=None) -> Optional[str]:
        query = str()

        if name:
            query = f'name={name}'

        if address:
            if not query:
                query = f'address={address}'
            else:
                query = f'{query}&address={address}'

        if stadium:
            if not query:
                query = f'stadium={stadium}'
            else:
                query = f'{query}&stadium={stadium}'

        if url:
            if not query:
                query = f'url={url}'
            else:
                query = f'{query}&url={url}'

        return query

    def __init__(self):
        """
        Constructor for a team service.
        """
        BaseService.__init__(self, TeamService.route_name)

    @classmethod
    def get_all(cls) -> List[Team]:
        """
        method to fetch all the teams in the database.
        """
        team_list: list = []
        team_res: dict = cls._get_items(cls.route_name)
        for item in team_res:
            team_list.append(Team(name=item['name'],
                                  address=item['address'],
                                  stadium=item['stadium'],
                                  url=item['url']))
        return team_list

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Team:
        """
        method to fetch a referee by id in the database
        """
        team_res: dict = cls._get_item_by_id(item_id, cls.route_name)
        new_team = Team(name=team_res['name'],
                        address=team_res['address'],
                        stadium=team_res['stadium'],
                        url=team_res['url'])
        return new_team

    @classmethod
    def add_item(cls, item_to_add: Team) -> int:
        """
            method to add a new team to the database.
        """
        team_dict = item_to_add.__dict__()
        response_status: int = cls._add_item(team_dict, cls.route_name)
        return response_status

    @classmethod
    def update_item_by_id(cls, item_id: int, item_data: Team) -> int:
        """
            method to update a team in the database
        """
        team_dict: dict = cls._create_dict(item_data)

        response_status: int = cls._update_item_by_id(item_id, team_dict, cls.route_name)
        return response_status

    @classmethod
    def delete_item_by_id(cls, item_id: int):
        """
            Delete a team from the database.
        """
        response_status: int = cls._delete_item_by_id(item_id, cls.route_name)
        return response_status

    @classmethod
    def search_items(cls, name=None, address=None, stadium=None, url=None) -> Optional[List[Team]]:
        """
            method to search all referees in the database based on their attributes.
        """
        query: str = cls._write_query(name=name,
                                       address=address,
                                       stadium=stadium,
                                       url=url)

        team_list: list = []
        team_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if team_res[1] != 404:
            for item in team_res[0]:
                team_list.append(Team(name=item['name'],
                                      address=item['address'],
                                      stadium=item['stadium'],
                                      url=item['url']))
        return team_list

    @classmethod
    def find_ids(cls, name=None, address=None, stadium=None, url=None):
        """
            return the id's of team objects in the database with the parameters requested by the user.
        """
        query: str = cls._write_query(name=name,
                                       address=address,
                                       stadium=stadium,
                                       url=url)

        team_list: list = []
        team_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if team_res[1] != 404:
            for item in team_res[0]:
                team_list.append({"id": item['id'],
                                  "name": item['name'],
                                  "address": item['address']})
        return team_list
