# Libraries:
from datetime import date
from app.models.base import db


# player class
from app.services.utils import none_to_empty


class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    home = db.Column(db.String(20), nullable=False)
    away = db.Column(db.String(50), nullable=False)
    day = db.Column(db.Date, nullable=False)
    result = db.Column(db.String(5), nullable=True)
    season_start = db.Column(db.Date, nullable=False)
    season_end = db.Column(db.Date, nullable=False)

    def __init__(self, home: str, away: str, day: date,
                 season_start: date, season_end: date, result: str = None) -> None:
        self.home = home
        self.away = away
        self.day = day
        self.season_start = season_start
        self.season_end = season_end
        self.result = result

    def __repr__(self):
        return f"Match between {self.home} and {self.away}, played on the {self.day}" \
               f"{none_to_empty(self.result, ' with a score of ')} during the season " \
               f"{self.season_start.year} - {self.season_end.year}."
