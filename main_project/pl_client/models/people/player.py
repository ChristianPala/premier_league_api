# Libraries.
from datetime import date
from pl_client.models.people.person import Person
from pl_client.services.utils import none_to_empty, date_to_string
from typing import Dict


class Player(Person):
    role_dictionary: Dict[str, str] = {'GK': 'goal keeper', 'DF': 'defender', 'MF': 'midfielder', 'FW': 'forward'}

    def __init__(self, name: str, role: str, surname: str = None, birth_date: date = None,
                 nationality: str = None, height: int = None) -> None:
        """
        Constructor for an object of type player
        :param name:
        :param role:
        :param surname:
        :param birth_date:
        :param nationality:
        :param height:
        """
        Person.__init__(self, name, surname, birth_date, nationality)
        self.__height = height
        self.__role = role

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, new_role) -> None:
        self.__role = new_role

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, new_height) -> None:
        self.__height = new_height

    def __dict__(self):
        """
            Dictionary representation of class player
        """
        height = None
        if self.height:
            height = str(self.height) + " cm"

        if self.birth_date is None:
            return {"name": self.name, "surname": self.surname, "birth_date": self.birth_date,
                    "nationality": self.nationality, "role": self.role, "height": self.height}

        return {"name": self.name,
                "surname": self.surname,
                "birth_date": date_to_string(self.birth_date),
                "nationality": self.nationality,
                "role": self.role,
                "height": height
                }

    def __repr__(self) -> str:
        """
            string representation for the player class.
        """
        height = None
        if self.height:
            height = str(self.height) + " cm"

        return f"{Person.__repr__(self)}{none_to_empty(height, ', he is ', ' tall')}" \
               f", playing as a {Player.role_dictionary[self.role]}"
