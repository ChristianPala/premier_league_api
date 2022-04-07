import pytest
from pl_client.models.people.person import Person
from pl_client.models.people.coach import Coach
from pl_client.models.people.player import Player
from pl_client.models.people.referee import Referee
from pl_client.models.team import Team
from pl_client.models.match_model import Match
from datetime import date


class TestClientPersonClass:
    def test_client_new_person_simple_case(self):
        """
        GIVEN a Person model
        WHEN a new Person is created
        THEN check the hash fields are defined correctly"""
        person = Person("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert person.name == "Christian"
        assert person.surname == "Pala"
        assert person.birth_date == date(1984, 1, 17)
        assert person.nationality == "Switzerland"

    def test_client_new_person_blank_case(self):
        """
        GIVEN a Person model
        WHEN a new Person is created with the minimum number of attributes required
        THEN check the hash fields are defined correctly."""
        person = Person("Christian")
        assert person.name == "Christian"
        assert person.surname is None
        assert person.birth_date is None
        assert person.nationality is None

    def test_client_new_person_should_fail_case(self):
        """
        GIVEN a Person model
        WHEN a new Person is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            person = Person()

    def test_client_person_representation_simple_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert person.__repr__() == "Christian Pala, born on the 17 of January 1984, from Switzerland"

    def test_client_person_representation_blank_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian")
        assert person.__repr__() == "Christian"

    def test_client_person_representation_birth_date_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian", birth_date=date(1984, 1, 17))
        assert person.__repr__() == "Christian, born on the 17 of January 1984"

    def test_client_person_representation_nationality_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian", nationality="Switzerland")
        assert person.__repr__() == "Christian, from Switzerland"

    def test_client_person_dictionary_simple_case(self):
        person = Person("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert person.__dict__() == {"name": "Christian", "surname": "Pala",
                                     "birth_date": "1984-01-17", "nationality": "Switzerland"}

    def test_client_person_dictionary_blank_case(self):
        person = Person("Christian")
        assert person.__dict__() == {"name": "Christian", "surname": None,
                                     "birth_date": None, "nationality": None}

    def test_client_calculate_age_1(self):
        person = Person("Christian", birth_date=date(1984, 1, 17))
        assert person.calculate_age() == 38

    def test_client_calculate_age_2(self):
        person = Person("Carlo", birth_date=date(2001, 5, 28))
        assert person.calculate_age() == 20

class TestClientCoachClass:
    def test_client_new_coach_simple_case(self):
        """
        GIVEN a Coach model
        WHEN a new Coach is created
        THEN check the hash fields are defined correctly."""
        coach = Coach("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert coach.name == "Christian"
        assert coach.surname == "Pala"
        assert coach.birth_date == date(1984, 1, 17)
        assert coach.nationality == "Switzerland"

    def test_client_new_coach_blank_case(self):
        """
        GIVEN a Coach model
        WHEN a new Coach is created wit the minimum number of attributes required
        THEN check the hash fields are defined correctly."""
        coach = Coach("Christian")
        assert coach.name == "Christian"
        assert coach.surname is None
        assert coach.birth_date is None
        assert coach.nationality is None

    def test_client_new_coach_should_fail_case(self):
        """
        GIVEN a Coach model
        WHEN a new Coach is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            coach = Coach()

    def test_client_coach_representation_simple_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert coach.__repr__() == "Christian Pala, born on the 17 of January 1984, from Switzerland"

    def test_client_coach_representation_blank_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian")
        assert coach.__repr__() == "Christian"

    def test_client_coach_representation_birth_date_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", birth_date=date(1984, 1, 17))
        assert coach.__repr__() == "Christian, born on the 17 of January 1984"

    def test_client_coach_representation_nationality_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", nationality="Switzerland")
        assert coach.__repr__() == "Christian, from Switzerland"

    def test_client_coach_dictionary_simple_case(self):
        """
        GIVEN a Coach model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert coach.__dict__() == {"name": "Christian",
                                    "surname": "Pala",
                                    "nationality": "Switzerland"}

    def test_client_coach_dictionary_blank_case(self):
        """
        GIVEN a Coach model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian")
        assert coach.__dict__() == {"name": "Christian",
                                    "surname": None,
                                    "nationality": None}

    def test_client_coach_dictionary_surname_case(self):
        """
        GIVEN a Coach model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", "Pala")
        assert coach.__dict__() == {"name": "Christian",
                                    "surname": "Pala",
                                    "nationality": None}

    def test_client_coach_dictionary_birth_date_case(self):
        """
        GIVEN a Coach model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", birth_date=date(1984, 1, 17))
        assert coach.__dict__() == {"name": "Christian",
                                    "surname": None,
                                    "nationality": None}

    def test_client_coach_dictionary_nationality_case(self):
        """
        GIVEN a Coach model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", nationality="Switzerland")
        assert coach.__dict__() == {"name": "Christian",
                                    "surname": None,
                                    "nationality": "Switzerland"}


class TestClientPlayerClass:
    def test_client_new_player_simple_case(self):
        """
        GIVEN a Player model
        WHEN a new Player is created
        THEN check the hash fields are defined correctly."""
        player = Player("Christian", "FW", "Pala", date(1984, 1, 17), "Switzerland", 187)
        assert player.name == "Christian"
        assert player.role == "FW"
        assert player.surname == "Pala"
        assert player.birth_date == date(1984, 1, 17)
        assert player.nationality == "Switzerland"
        assert player.height == 187

    def test_client_new_player_blank_case(self):
        """
        GIVEN a Player model
        WHEN a new Player is created with the minimum number of attributes required
        THEN check the hash fields are defined correctly."""
        player = Player("Christian", "FW")
        assert player.name == "Christian"
        assert player.role == "FW"
        assert player.surname is None
        assert player.birth_date is None
        assert player.nationality is None

    def test_client_new_player_should_fail_case(self):
        """
        GIVEN a Player model
        WHEN a new Player is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            player = Player("Christian")

    def test_client_new_player_should_fail_case_2(self):
        """
        GIVEN a Player model
        WHEN a new Player is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            player = Player(role="FW")

    def test_client_new_player_should_fail_case_3(self):
        """
        GIVEN a Player model
        WHEN a new Player is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            player = Player()

    def test_client_player_representation_simple_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", "Pala", date(1984, 1, 17), "Switzerland", 187)
        assert player.__repr__() == "Christian Pala, " \
                                    "born on the 17 of January 1984, from Switzerland, he is 187 cm tall, " \
                                    "playing as a forward"

    def test_client_player_representation_blank_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW")
        assert player.__repr__() == "Christian, playing as a forward"

    def test_client_player_representation_birth_date_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", birth_date=date(1984, 1, 17))
        assert player.__repr__() == "Christian, born on the 17 of January 1984, playing as a forward"

    def test_client_player_representation_nationality_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", nationality="Switzerland")
        assert player.__repr__() == "Christian, from Switzerland, playing as a forward"

    def test_client_player_dictionary_simple_case(self):
        """
        GIVEN a Player model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", "Pala", date(1984, 1, 17), "Switzerland", 187)
        assert player.__dict__() == {"name": "Christian",
                                     "surname": "Pala",
                                     "birth_date": "1984-01-17",
                                     "nationality": "Switzerland",
                                     "height": "187 cm",
                                     "role": "FW"}

    def test_client_player_dictionary_blank_case(self):
        """
        GIVEN a Player model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW")
        assert player.__dict__() == {"name": "Christian",
                                     "surname": None,
                                     "birth_date": None,
                                     "nationality": None,
                                     "height": None,
                                     "role": "FW"}

    def test_client_player_dictionary_surname_case(self):
        """
        GIVEN a Player model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", surname="Pala")
        assert player.__dict__() == {"name": "Christian",
                                     "surname": "Pala",
                                     "birth_date": None,
                                     "nationality": None,
                                     "height": None,
                                     "role": "FW"}

    def test_client_player_dictionary_birth_date_case(self):
        """
        GIVEN a Player model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", birth_date=date(1984, 1, 17))
        assert player.__dict__() == {"name": "Christian",
                                     "surname": None,
                                     "birth_date": "1984-01-17",
                                     "nationality": None,
                                     "height": None,
                                     "role": "FW"}

    def test_client_player_dictionary_nationality_case(self):
        """
        GIVEN a Player model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", nationality="Switzerland")
        assert player.__dict__() == {"name": "Christian",
                                     "surname": None,
                                     "birth_date": None,
                                     "nationality": "Switzerland",
                                     "height": None,
                                     "role": "FW"}


class TestClientRefereeClass:
    def test_client_new_referee_simple_case(self):
        """
        GIVEN a Referee model
        WHEN a new Referee is created
        THEN check the hash fields are defined correctly-"""
        referee = Referee("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert referee.name == "Christian"
        assert referee.surname == "Pala"
        assert referee.birth_date == date(1984, 1, 17)
        assert referee.nationality == "Switzerland"

    def test_client_new_referee_blank_case(self):
        """
        GIVEN a Referee model
        WHEN a new Referee is created with the minimum number of attributes required
        THEN check it raises a TypeError."""
        referee = Referee("Christian")
        assert referee.name == "Christian"
        assert referee.surname is None
        assert referee.birth_date is None
        assert referee.nationality is None

    def test_client_new_referee_should_fail_case(self):
        """
        GIVEN a Referee model
        WHEN a new Referee is created
        THEN check the hash fields are defined correctly"""
        with pytest.raises(TypeError):
            referee = Referee()

    def test_client_referee_representation_simple_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert referee.__repr__() == "Christian Pala, born on the 17 of January 1984, from Switzerland"

    def test_client_referee_representation_blank_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian")
        assert referee.__repr__() == "Christian"

    def test_client_referee_representation_birth_date_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", birth_date=date(1984, 1, 17))
        assert referee.__repr__() == "Christian, born on the 17 of January 1984"

    def test_client_referee_representation_nationality_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", nationality="Switzerland")
        assert referee.__repr__() == "Christian, from Switzerland"

    def test_client_referee_dictionary_simple_case(self):
        """
        GIVEN a Referee model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert referee.__dict__() == {"name": "Christian",
                                      "surname": "Pala",
                                      "birth_date": "1984-01-17",
                                      "nationality": "Switzerland"}

    def test_client_referee_dictionary_blank_case(self):
        """
        GIVEN a Referee model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian")
        assert referee.__dict__() == {"name": "Christian",
                                      "surname": None,
                                      "birth_date": None,
                                      "nationality": None}

    def test_client_referee_dictionary_surname_case(self):
        """
        GIVEN a Referee model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", "Pala")
        assert referee.__dict__() == {"name": "Christian",
                                      "surname": "Pala",
                                      "birth_date": None,
                                      "nationality": None}

    def test_client_referee_dictionary_birth_date_case(self):
        """
        GIVEN a Referee model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", birth_date=date(1984, 1, 17))
        assert referee.__dict__() == {"name": "Christian",
                                      "surname": None,
                                      "birth_date": "1984-01-17",
                                      "nationality": None}

    def test_client_referee_dictionary_nationality_case(self):
        """
        GIVEN a Referee model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", nationality="Switzerland")
        assert referee.__dict__() == {"name": "Christian",
                                      "surname": None,
                                      "birth_date": None,
                                      "nationality": "Switzerland"}


class TestClientTeamClass:

    def test_client_new_team_simple_case(self):
        """
        GIVEN a Team model
        WHEN a new Team is created
        THEN check the hash fields are defined correctly-"""
        team = Team("Arsenal FC", "Baker Street 13, London", "Old Trafford", "www.arsenal.co.uk")
        assert team.name == "Arsenal FC"
        assert team.address == "Baker Street 13, London"
        assert team.stadium == "Old Trafford"
        assert team.url == "www.arsenal.co.uk"

    def test_client_new_team_blank_case(self):
        """
        GIVEN a Team model
        WHEN a new Team is created
        THEN check the hash fields are defined correctly-"""
        team = Team("Arsenal FC", "Baker Street 13, London")
        assert team.name == "Arsenal FC"
        assert team.address == "Baker Street 13, London"
        assert team.stadium is None
        assert team.url is None

    def test_client_new_team_should_fail_case(self):
        """
        GIVEN a Team model
        WHEN a new Team is created
        THEN check the hash fields are defined correctly"""
        with pytest.raises(TypeError):
            team = Team()

    def test_client_team_representation_simple_case(self):
        """
        GIVEN a Team model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London", "Old Trafford", "www.arsenal.co.uk")
        assert team.__repr__() == "Arsenal FC, located at Baker Street 13, London, playing at Old Trafford, " \
                                  "whose web page is: www.arsenal.co.uk"

    def test_client_team_representation_blank_case(self):
        """
        GIVEN a Team model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London")
        assert team.__repr__() == "Arsenal FC, located at Baker Street 13, London"

    def test_client_team_dictionary_simple_case(self):
        """
        GIVEN a Team model
        WHEN the dictionary method is called
        THEN check the desired dictionary is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London", "Old Trafford", "www.arsenal.co.uk")
        assert team.__dict__() == {"name": "Arsenal FC",
                                   "address": "Baker Street 13, London",
                                   "stadium": "Old Trafford",
                                   "url": "www.arsenal.co.uk"}

    def test_client_team_dictionary_blank_case(self):
        """
        GIVEN a Team model
        WHEN the dictionary method is called
        THEN check the desired dictionary is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London")
        assert team.__dict__() == {"name": "Arsenal FC",
                                   "address": "Baker Street 13, London",
                                   "stadium": None,
                                   "url": None}

    def test_client_team_dictionary_stadium_case(self):
        """
        GIVEN a Team model
        WHEN the dictionary method is called
        THEN check the desired dictionary is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London", stadium="Old Trafford", )
        assert team.__dict__() == {"name": "Arsenal FC",
                                   "address": "Baker Street 13, London",
                                   "stadium": "Old Trafford",
                                   "url": None}

    def test_client_team_dictionary_url_case(self):
        """
        GIVEN a Referee model
        WHEN the dictionary method is called
        THEN check the desired string is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London", url="www.arsenal.co.uk")
        assert team.__dict__() == {"name": "Arsenal FC",
                                   "address": "Baker Street 13, London",
                                   "stadium": None,
                                   "url": "www.arsenal.co.uk"}


class TestClientMatchClass:

    def test_client_new_match_simple_case(self):
        """
        GIVEN a Match model
        WHEN a new Match is created
        THEN check the hash fields are defined correctly-"""
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22), "1-0")
        assert match.home == "Arsenal FC"
        assert match.away == "Chelsea"
        assert match.day == date(1995, 3, 15)
        assert match.result == "1-0"

    def test_client_new_match_blank_case(self):
        """
        GIVEN a Match model
        WHEN a new Match is created
        THEN check the hash fields are defined correctly-"""
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22))
        assert match.home == "Arsenal FC"
        assert match.away == "Chelsea"
        assert match.day == date(1995, 3, 15)
        assert match.result is None

    def test_client_new_match_should_fail_case(self):
        """
        GIVEN a Match model
        WHEN a new Match is created
        THEN check the hash fields are defined correctly"""
        with pytest.raises(TypeError):
            match = Match()

    def test_client_match_representation_simple_case(self):
        """
        GIVEN a Match model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22), "1-0")
        assert match.__repr__() == "Match between Arsenal FC and Chelsea, played on the 15 of March 1995 with a score of 1-0" \
                                   " during the season 2021 - 2022"

    def test_client_match_representation_blank_case(self):
        """
        GIVEN a Match model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22))
        assert match.__repr__() == "Match between Arsenal FC and Chelsea, played on the 15 of March 1995 during the season" \
                                   " 2021 - 2022"

    def test_client_match_dictionary_simple_case(self):
        """
        GIVEN a Match model
        WHEN the dictionary method is called
        THEN check the desired dictionary is outputted.
        """
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22), "1-0")
        assert match.__dict__() == {"home": "Arsenal FC",
                                    "away": "Chelsea",
                                    "day": "1995-03-15",
                                    "season_start": "2021-08-13",
                                    "season_end": "2022-05-22",
                                    "result": "1-0"}

    def test_client_match_dictionary_blank_case(self):
        """
        GIVEN a Match model
        WHEN the dictionary method is called
        THEN check the desired dictionary is outputted.
        """
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22))
        assert match.__dict__() == {"home": "Arsenal FC",
                                    "away": "Chelsea",
                                    "day": "1995-03-15",
                                    "season_start": "2021-08-13",
                                    "season_end": "2022-05-22",
                                    "result": None}
