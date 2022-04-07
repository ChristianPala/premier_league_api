# Libraries:
from app.models.base import db
from app.services.utils import none_to_empty


# team model class
class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    stadium = db.Column(db.String(50), nullable=True)
    url = db.Column(db.String(50), unique=True, nullable=True)

    def __init__(self, name: str, address: str, stadium: str = None, url: str = None) -> None:
        self.name = name
        self.address = address
        self.stadium = stadium
        self.url = url

    def __repr__(self) -> str:
        """string representation for the player class."""
        return f"Team {self.name}, located: {self.address}{none_to_empty(self.stadium,' playing at ')}" \
               f"{none_to_empty(self.url,', whose web page is: ')}."
