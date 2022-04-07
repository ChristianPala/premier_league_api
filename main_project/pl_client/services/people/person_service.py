from abc import ABC
from pl_client.services.base_service import BaseService
from pl_client.services.utils import date_to_string
from typing import Dict, Any, List, Type, Union, Optional

# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class PersonService(BaseService, ABC):
    """
        Abstract person class to model all objects of type person in the premier league database.
    """

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

    def __init__(self, route_name):
        BaseService.__init__(self, route_name)
