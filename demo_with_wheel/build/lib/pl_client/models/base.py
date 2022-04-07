# Libraries:
from abc import ABC, abstractmethod


# Interface for all services to ensure they have string and dictionary representations.
class Base(ABC):

    @abstractmethod
    def __repr__(self):
        """
            method to ensure all children have a string representation
        """
        pass

    @abstractmethod
    def __dict__(self):
        """
            method to ensure all children have a dictionary representation.
        """
        pass
