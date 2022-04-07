# Libraries:
from datetime import date
from pl_client.services.utils import none_to_empty, date_to_string, date_to_long_string
from pl_client.models.base import Base


class Match(Base):
    """
    Match model class for the premier league api client library.
    """

    def __init__(self, home: str, away: str, day: date,
                 season_start: date, season_end: date, result: str = None) -> None:
        """
        Constructor for an object of type match.
        :param home:
        :param away:
        :param day:
        :param season_start:
        :param season_end:
        :param result:
        """
        self.home = home
        self.away = away
        self.day = day
        self.season_start = season_start
        self.season_end = season_end
        self.result = result

    @property
    def home(self) -> str:
        return self.__home

    @home.setter
    def home(self, home: str) -> None:
        self.__home = home

    @property
    def away(self) -> str:
        return self.__away

    @away.setter
    def away(self, away_team) -> None:
        self.__away = away_team

    @property
    def day(self) -> date:
        return self.__day

    @day.setter
    def day(self, match_day: date) -> None:
        self.__day = match_day

    @property
    def season_start(self) -> date:
        return self.__season_start

    @season_start.setter
    def season_start(self, season_start: date) -> None:
        self.__season_start = season_start

    @property
    def season_end(self) -> date:
        return self.__season_end

    @season_end.setter
    def season_end(self, season_end: date) -> None:
        self.__season_end = season_end

    @property
    def result(self) -> str:
        return self.__result

    @result.setter
    def result(self, new_result: str) -> None:
        self.__result = new_result

    def __repr__(self):
        """
            String representation of class match.
        """
        return f"Match between {self.home} and {self.away}, played on the {date_to_long_string(self.day)}" \
               f"{none_to_empty(self.result, ' with a score of ')} during the season " \
               f"{self.season_start.year} - {self.season_end.year}"

    def __dict__(self) -> dict:
        """
            Dictionary representation of class match
        """
        return {"home": self.home,
                "away": self.away,
                "day": date_to_string(self.day),
                "season_start": date_to_string(self.season_start),
                "season_end": date_to_string(self.season_end),
                "result": self.result
                }
