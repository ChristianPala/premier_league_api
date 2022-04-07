# Todo: Put all utility functions needed in the other packages here.
from datetime import date
from flask import request, jsonify

from typing import Union,  Dict, Any, List, Type

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


# functions:
def none_to_empty(my_string, prepend: str = "", append: str = "") -> str:

    if isinstance(my_string, date):
        my_string = str(my_string)

    return "" if my_string is None else prepend + my_string + append



