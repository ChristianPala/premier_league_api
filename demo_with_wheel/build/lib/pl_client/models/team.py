# Libraries:
from pl_client.models.base import Base
from pl_client.services.utils import none_to_empty


class Team(Base):

    def __init__(self, name: str, address: str, stadium: str = None, url: str = None) -> None:
        """
        Constructor for an object of type team.
        :param name:
        :param address:
        :param stadium:
        :param url:
        """
        self.__name = name
        self.__address = address
        self.__stadium = stadium
        self.__url = url

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def stadium(self):
        return self.__stadium

    @stadium.setter
    def stadium(self, value):
        self.__stadium = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    def __repr__(self):
        """string representation for the player class."""
        return f"{self.name}, located at {self.address}{none_to_empty(self.stadium, ', playing at ', ', ')}" \
               f"{none_to_empty(self.url, 'whose web page is: ')}"

    def __dict__(self) -> dict:
        """
            Dictionary representation of class team
        """
        return {"name": self.name,
                "address": self.address,
                "stadium": self.stadium,
                "url": self.url
                }
