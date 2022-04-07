# Libraries:
from abc import ABC
from datetime import date
from pl_client.services.utils import none_to_empty, date_to_string
from pl_client.models.base import Base


# Blueprint for a person:
class Person(Base, ABC):
    def __init__(self, name: str, surname: str = None, birth_date: date = None,
                 nationality: str = None) -> None:
        """
        Constructor for an abstract person object
        :param name:
        :param surname:
        :param birth_date:
        :param nationality:
        """
        self.__name = name
        self.__surname = surname
        self.__birth_date = birth_date
        self.__nationality = nationality

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, new_surname) -> None:
        self.__surname = new_surname

    @property
    def birth_date(self) -> date:
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, new_date) -> None:
        self.__birth_date = new_date

    @property
    def nationality(self) -> str:
        return self.__nationality

    @nationality.setter
    def nationality(self, new_nationality) -> None:
        self.__nationality = new_nationality

    def __repr__(self) -> str:
        """
            string representation of class person
        """
        return f"{self.name}{none_to_empty(self.surname, ' ')}{none_to_empty(self.birth_date, ', born on the ')}" \
               f"{none_to_empty(self.nationality, ', from ')}"

    def __dict__(self) -> dict:
        """
            Dictionary representation of class person
        """
        if self.birth_date is None:
            return {"name": self.name,
                    "surname": self.surname,
                    "birth_date": self.birth_date,
                    "nationality": self.nationality}

        return {"name": self.name, "surname": self.surname,
                "birth_date": date_to_string(self.birth_date),
                "nationality": self.nationality}

    def calculate_age(self) -> int:
        """
            Calculates the current age of the person
        """
        today = date.today()
        age: int = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month,
                                                                                    self.birth_date.day))
        return age
