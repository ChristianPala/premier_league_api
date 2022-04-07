# Libraries:
from pl_client.services.base_service import BaseService
from pl_client.models.match_model import Match
from pl_client.services.utils import string_to_date, date_to_string
from typing import Dict, Any, List, Type, Union, Optional, Tuple


# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class MatchService(BaseService):
    """
        match service class to interact between the client model request and the Flask API.
    """

    route_name = 'matches'

    @classmethod
    def _create_dict(cls, item_data: Any):
        model_dict = dict()
        if item_data.home:
            model_dict.update({"home": item_data.home})

        if item_data.away:
            model_dict.update({"away": item_data.away})

        if item_data.day:
            model_dict.update({"day": date_to_string(item_data.day)})

        if item_data.season_start:
            model_dict.update({"season_start": date_to_string(item_data.season_start)})

        if item_data.season_end:
            model_dict.update({"season_end": date_to_string(item_data.season_end)})

        return model_dict

    @classmethod
    def _write_query(cls, home=None,
                    away=None,
                    day=None,
                    season_start=None,
                    season_end=None,
                    result=None) -> Optional[str]:

        query = str()

        if home:
            query = f'home={home}'

        if away:
            if not query:
                query = f'away={away}'
            else:
                query = f'{query}&away={away}'

        if day:
            if not query:
                query = f'day={day}'
            else:
                query = f'{query}&day={day}'

        if season_start:
            if not query:
                query = f'season_start={season_start}'
            else:
                query = f'{query}&season_start={season_start}'

        if season_end:
            if not query:
                query = f'season_end={season_end}'
            else:
                query = f'{query}&season_end={season_end}'

        if result:
            if not query:
                query = f'result={result}'
            else:
                query = f'{query}&result={result}'

        return query

    def __init__(self) -> None:
        """
        Constructor for a match service.
        """
        BaseService.__init__(self, MatchService.route_name)

    @classmethod
    def get_all(cls) -> List[Match]:
        """
            method to return all players in the database.
        """
        player_list: list = []
        player_res: dict = cls._get_items(cls.route_name)
        for item in player_res:
            player_list.append(Match(home=item['home'],
                                     away=item['away'],
                                     day=string_to_date(item['day']),
                                     season_start=string_to_date(item['season_start']),
                                     season_end=string_to_date(item['season_end']),
                                     result=item['result']))
        return player_list

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Match:
        """
        method to fetch a referee by id in the database
        """
        match_res: dict = cls._get_item_by_id(item_id, cls.route_name)
        new_match = Match(home=match_res['home'],
                          away=match_res['away'],
                          day=string_to_date(match_res['day']),
                          season_start=string_to_date(match_res['season_start']),
                          season_end=string_to_date(match_res['season_end']),
                          result=match_res['result'])

        return new_match

    @classmethod
    def add_item(cls, item_to_add: Match) -> int:
        """
            method to add a referee to the database
        """
        match_dict = item_to_add.__dict__()
        response_status: int = cls._add_item(match_dict, cls.route_name)
        return response_status

    @classmethod
    def update_item_by_id(cls, item_id: int, item_data: Match) -> int:
        """
            method to update a referee in the database
        """
        match_dict: dict = cls._create_dict(item_data)

        response_status: int = cls._update_item_by_id(item_id, match_dict, cls.route_name)
        return response_status

    @classmethod
    def delete_item_by_id(cls, item_id: int) -> int:
        """
            method to delete a match from the database
        """
        response_status: int = cls._delete_item_by_id(item_id, cls.route_name)
        return response_status

    @classmethod
    def search_items(cls, home=None, away=None, day=None, season_start=None, season_end=None,
                     result=None) -> Optional[List[Match]]:

        query: str = cls._write_query(home=home,
                                       away=away,
                                       day=day,
                                       season_start=season_start,
                                       season_end=season_end,
                                       result=result)
        match_list: list = []
        match_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if match_res[1] != 404:
            for item in match_res[0]:
                match_list.append(Match(home=item['home'],
                                        away=item['away'],
                                        day=string_to_date(item['day']),
                                        season_start=string_to_date(item['season_start']),
                                        season_end=string_to_date(item['season_end']),
                                        result=item['result']))
        return match_list

    @classmethod
    def find_ids(cls, home=None, away=None, day=None, season_start=None, season_end=None, result=None) -> List[Dict]:
        """
            return the id's of team objects in the database with the parameters requested by the user.
        """
        query: str = cls._write_query(home=home,
                                       away=away,
                                       day=day,
                                       season_start=season_start,
                                       season_end=season_end,
                                       result=result)

        match_list: list = []
        match_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if match_res[1] != 404:
            for item in match_res[0]:
                match_list.append({"id": item['id'],
                                  "home": item['home'],
                                  "away": item['away'],
                                  "day": string_to_date(item['day']),
                                  "season_start": string_to_date(item['season_start']),
                                  "season_end": string_to_date(item['season_end'])})
        return match_list
