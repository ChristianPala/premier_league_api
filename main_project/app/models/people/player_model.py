# Libraries:
from datetime import date
from app.models.people.person_model import Person
from app.services.utils import none_to_empty
from app.models.people.person_model import db
from typing import Dict


# player class
class Player(Person):
    """
    Player model class.
    """
    __tablename__ = 'player'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(10), nullable=True)
    role = db.Column(db.String(20), nullable=False)

    def __init__(self, name: str, role: str, surname: str = None, birth_date: date = None, nationality: str = None,
                 height: str = None) -> None:
        Person.__init__(self, name, surname, birth_date, nationality)
        self.height = height
        self.role = role

    def __repr__(self) -> str:
        """string representation for the player class."""
        return f"Player {Person.__repr__(self)}{none_to_empty(self.height, ' is ',' tall')}, playing as " \
               f"{Player.__role_dictionary[self.role]}."

    __role_dictionary: Dict[str, str] = {'GK': 'goal keeper', 'DF': 'defender', 'MF': 'midfielder', 'FW': 'forward'}
