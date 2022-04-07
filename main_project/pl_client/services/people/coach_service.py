from pl_client.services.people.person_service import PersonService
from pl_client.models.people.coach import Coach
from typing import List, Optional, Tuple, Union, Type, Any, Dict
from pl_client.services.utils import date_to_string

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class CoachService(PersonService):
    """
    class that extends the person server business logic for coach models.
    """
    route_name = 'coaches'

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

        return model_dict

    def __init__(self) -> None:
        PersonService.__init__(self, CoachService.route_name)

    @classmethod
    def get_all(cls) -> List[Coach]:
        """
            method to get all coaches in the database.
        """
        coach_list: list = []
        coach_res: dict = cls._get_items(cls.route_name)
        for item in coach_res:
            coach_list.append(Coach(name=item['name'], surname=item['surname'], nationality=item['nationality']))
        return coach_list

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Coach:
        """
        method to fetch a coach by id in the database.
        """
        coach_res: dict = cls._get_item_by_id(item_id, cls.route_name)
        new_coach = Coach(name=coach_res['name'], surname=coach_res['surname'], nationality=coach_res['nationality'])
        return new_coach

    @classmethod
    def add_item(cls, item_to_add: Coach) -> int:
        """
            method to add a coach to the database.
        """
        coach_dict = item_to_add.__dict__()
        response_status: int = cls._add_item(coach_dict, cls.route_name)
        return response_status

    @classmethod
    def update_item_by_id(cls, item_id: int, item_data: Coach) -> int:
        """
            method to update a coach by id in the database.
        """
        coach_dict: dict = cls._create_dict(item_data)
        response_status: int = cls._update_item_by_id(item_id, coach_dict, cls.route_name)
        return response_status

    @classmethod
    def delete_item_by_id(cls, item_id: int) -> int:
        """
            method to delete a coach by id from the database
        """
        response_status: int = cls._delete_item_by_id(item_id, cls.route_name)
        return response_status

    @classmethod
    def search_items(cls, name=None, surname=None, nationality=None) -> Optional[List[Coach]]:
        """
            method to search all coaches filtering by their attributes.
        """
        query: str = cls._write_query(name=name, surname=surname, nationality=nationality)
        coach_list: list = []
        coach_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if coach_res[1] != 404:
            for item in coach_res[0]:
                coach_list.append(Coach(name=item['name'], surname=item['surname'], nationality=item['nationality']))
        return coach_list

    @classmethod
    def find_ids(cls, name=None, surname=None, nationality=None):
        """
            return the id's of coach objects in the database with the parameters requested by the user.
        """
        query: str = cls._write_query(name=name, surname=surname, nationality=nationality)

        coach_list: list = []
        coach_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if coach_res[1] != 404:
            for item in coach_res[0]:
                coach_list.append({"id": item['id'], "name": item['name'], "surname": item['surname']})
        return coach_list
