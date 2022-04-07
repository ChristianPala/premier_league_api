from pl_client.services.people.person_service import PersonService
from pl_client.models.people.referee import Referee
from pl_client.services.utils import string_to_date
from typing import List, Optional, Tuple, Union, Type, Any, Dict


JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class RefereeService(PersonService):
    """
    Blueprint for a referee.
    """
    route_name = 'referees'

    def __init__(self) -> None:
        """
        Constructor for an object of type referee.
        """
        PersonService.__init__(self, RefereeService.route_name)

    @classmethod
    def get_all(cls) -> List[Referee]:
        """
            method to return a list of all referees in the database.
        """
        referee_list: list = []
        referee_res: dict = cls._get_items(cls.route_name)
        for item in referee_res:
            referee_list.append(Referee(name=item['name'], surname=item['surname'],
                                        birth_date=string_to_date(item['birth_date']),
                                        nationality=item['nationality']))
        return referee_list

    @classmethod
    def get_item_by_id(cls, item_id: int) -> Referee:
        """
        method to fetch a referee by id in the database
        """
        referee_res: dict = cls._get_item_by_id(item_id, cls.route_name)
        new_referee = Referee(name=referee_res['name'], surname=referee_res['surname'],
                              birth_date=string_to_date(referee_res['birth_date']),
                              nationality=referee_res['nationality'])
        return new_referee

    @classmethod
    def add_item(cls, item_to_add: Referee) -> int:
        """
            method to add a referee to the database
        """
        referee_dict = item_to_add.__dict__()
        response_status: int = cls._add_item(referee_dict, cls.route_name)
        return response_status

    @classmethod
    def update_item_by_id(cls, item_id: int, item_data: Referee) -> int:
        """
            method to update a referee in the database
        """
        referee_dict: dict = cls._create_dict(item_data)

        response_status: int = cls._update_item_by_id(item_id, referee_dict, cls.route_name)
        return response_status

    @classmethod
    def delete_item_by_id(cls, item_id: int) -> int:
        """
            method to delete a referee from the database
        """
        response_status: int = cls._delete_item_by_id(item_id, cls.route_name)
        return response_status

    @classmethod
    def search_items(cls, name=None, surname=None, birth_date=None, nationality=None) -> Optional[List[Referee]]:
        """
            method to search all referees in the database based on their attributes.
        """
        query: str = cls._write_query(name=name,
                                     surname=surname,
                                     birth_date=birth_date,
                                     nationality=nationality)

        referee_list: list = []
        referee_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if referee_res[1] != 404:
            for item in referee_res[0]:
                referee_list.append(Referee(name=item['name'], surname=item['surname'],
                                            birth_date=string_to_date(item['birth_date']),
                                            nationality=item['nationality']))
        return referee_list

    @classmethod
    def find_ids(cls, name=None, surname=None, birth_date=None, nationality=None):
        """
            return the id's of referee objects in the database with the parameters requested by the user.
        """
        query: str = cls._write_query(name=name,
                                       surname=surname,
                                       birth_date=birth_date,
                                       nationality=nationality,
                                       )
        referee_list: list = []
        referee_res: Tuple[List[JSON], int] = cls._search_items(query, cls.route_name)
        if referee_res[1] != 404:
            for item in referee_res[0]:
                referee_list.append({"id": item['id'], "name": item['name'], "surname": item['surname']})
        return referee_list
