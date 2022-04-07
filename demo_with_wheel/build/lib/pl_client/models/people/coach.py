# Libraries:
from datetime import date
from pl_client.models.people.person import Person


# Blueprint for a coach.
class Coach(Person):

    def __init__(self, name: str, surname: str = None, birth_date: date = None,
                 nationality: str = None) -> None:
        """
        Constructor for an object of type coach:
        :param name:
        :param surname:
        :param birth_date:
        :param nationality:
        """

        Person.__init__(self, name, surname, birth_date, nationality)

    def __repr__(self) -> str:
        """
        string representation for the coach class.
        """
        return f'{Person.__repr__(self)}'

    def __dict__(self) -> dict:
        """
        dictionary representation for the coach class
        """
        return {"name": self.name,
                "surname": self.surname,
                "nationality": self.nationality}



