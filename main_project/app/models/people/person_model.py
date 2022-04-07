# Libraries:
from datetime import date
from app.services.utils import none_to_empty
from app.models.base import db


class Person(db.Model):
    """
    Abstract person model class.
    """
    __abstract__ = True
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    nationality = db.Column(db.String(20), nullable=True)

    def __init__(self, name: str, surname: str = None, birth_date: date = None, nationality: str = None):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.nationality = nationality

    def __repr__(self):
        return f"{self.name}{none_to_empty(self.surname,' ')}{none_to_empty(self.birth_date,', born ')}" \
               f"{none_to_empty(self.nationality, ' from ')}"

