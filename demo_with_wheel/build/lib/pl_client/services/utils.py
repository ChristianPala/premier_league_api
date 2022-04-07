# Libraries:
from datetime import date, datetime
from typing import Union, Dict, Any, List, Type, Optional

# Custom JSON type hint:
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


#    Utility functions repository for clients, code duplication with app done to keep the two parts of the project
#    separate.

def string_to_date(date_string: str) -> Optional[date]:
    """
        Utility function.
        Changes a YYYY-MM-DD string, to a date as it is saved in models.
    """
    if date_string is not None:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    else:
        return date_string


def date_to_string(date_object: date) -> str:
    """
        Utility function.
        Changes a date to a YYYY-MM-DD string, as it is passed through requests: 1900-01-01.
    """
    return date_object.strftime('%Y-%m-%d')


def date_to_long_string(date_object: date) -> str:
    """
    Utility function for none_to_empty and __repr__.
    Changes a date to a string in a readable format: 1 January 1900.
    """
    transformed_string = date_object.strftime('%d of %B %Y')
    if transformed_string[0] == '0':
        return transformed_string[1:]
    return transformed_string


def none_to_empty(my_string, prepend: str = "", append: str = "") -> str:
    """
    Utility function for __repr__.
    Changes date objects to strings, then if the string is not empty prepends and appends strings from arguments,
    if it is None it returns an empty string
    """
    if isinstance(my_string, date):

        my_string = date_to_long_string(my_string)
        if my_string[0] == '0':
            my_string = my_string[1:]

    return "" if my_string is None or my_string == "" else prepend + str(my_string) + append
