# Libraries:
from abc import ABC, abstractmethod
from pl_client.database.api_connection_information import api_url
import requests
from typing import Dict, Any, List, Type, Union, Tuple

# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class BaseService(ABC):

    @staticmethod
    def _get_items(route_name: str) -> JSON:
        """
        method to fetch all items in the database.
        """
        items: List[JSON] = requests.get(f'{api_url}{route_name}').json()
        return items

    @staticmethod
    def _get_item_by_id(item_id: int, route_name: str) -> JSON:
        """
        method to fetch an item by id from the API.
        """
        item: JSON = requests.get(f"{api_url}{route_name}/{item_id}").json()
        return item

    @staticmethod
    def _add_item(item: dict, route_name: str) -> int:
        """
        method to add an item to the database.
        """
        print(f'BaseService:{item}')
        print(f'{api_url}{route_name}')
        request = requests.post(f'{api_url}{route_name}', json=item)
        return request.status_code

    @staticmethod
    def _delete_item_by_id(item_id: int, route_name: str) -> int:
        """
        method to delete an item from the database.
        """
        request = requests.delete(f'{api_url}{route_name}/{item_id}')
        return request.status_code

    @staticmethod
    def _update_item_by_id(item_id, item, route_name) -> int:
        """
        method to update an item by id.
        """
        request = requests.put(f'{api_url}{route_name}/{item_id}', json=item)
        return request.status_code

    @staticmethod
    def _search_items(query: str, route_name: str) -> Tuple[List[JSON], int]:
        """
        method to search an item by all exposed fields.
        """
        print(f'query:{query}')
        response = requests.get(f'{api_url}{route_name}/search?{query}')
        if response.status_code != 404:
            items = response.json()
        else:
            items = []
        return items, response.status_code

    @classmethod
    @abstractmethod
    def _write_query(cls):
        pass

    @classmethod
    @abstractmethod
    def get_all(cls):
        pass

    @classmethod
    @abstractmethod
    def get_item_by_id(cls, item_id: int):
        pass

    @classmethod
    @abstractmethod
    def add_item(cls, item_to_add):
        pass

    @classmethod
    @abstractmethod
    def update_item_by_id(cls, item_id: int, item_data):
        pass

    @classmethod
    @abstractmethod
    def delete_item_by_id(cls, item_id):
        pass

    @classmethod
    @abstractmethod
    def search_items(cls):
        pass

    def __init__(self, route_name) -> None:
        """
        constructor for a generic service.
        """
        self.route_name = route_name

    @classmethod
    @abstractmethod
    def find_ids(cls):
        """
            Ensure all classes have a way to tell the client what id they have.
        """
        pass

    @classmethod
    @abstractmethod
    def _create_dict(cls, item_data):
        """
            Ensure all classes have a way to tell the client what id they have.
        """
        pass

    @property
    def route_name(self):
        return self.__route_name

    @route_name.setter
    def route_name(self, value):
        self.__route_name = value
