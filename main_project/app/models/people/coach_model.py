# Libraries:
from datetime import date
from app.models.people.person_model import Person
from app.models.people.person_model import db


# referee class
class Coach(Person):
    """
    Coach model class.
    """
    __tablename__ = 'coach'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name: str, surname: str = None, birth_date: date = None
                 , nationality: str = None) -> None:
        Person.__init__(self, name, surname, birth_date, nationality)

    def __repr__(self):
        return f"Coach {Person.__repr__(self)}."

