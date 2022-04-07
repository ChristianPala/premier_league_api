import pytest
from datetime import date
from app.models.people.coach_model import Coach
from app.models.people.person_model import Person
from app.models.people.player_model import Player
from app.models.people.referee_model import Referee
from app.models.team_model import Team
from app.models.match_model import Match


class TestPersonClass:
    def test_new_person_simple_case(self):
        """
        GIVEN a Person model
        WHEN a new Person is created
        THEN check the hash fields are defined correctly"""
        person = Person("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert person.name == "Christian"
        assert person.surname == "Pala"
        assert person.birth_date == date(1984, 1, 17)
        assert person.nationality == "Switzerland"

    def test_new_person_blank_case(self):
        """
        GIVEN a Person model
        WHEN a new Person is created with the minimum number of attributes required
        THEN check the hash fields are defined correctly."""
        person = Person("Christian")
        assert person.name == "Christian"
        assert person.surname is None
        assert person.birth_date is None
        assert person.nationality is None

    def test_new_person_should_fail_case(self):
        """
        GIVEN a Person model
        WHEN a new Person is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            person = Person()

    def test_person_representation_simple_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert person.__repr__() == "Christian Pala, born 1984-01-17 from Switzerland"

    def test_person_representation_blank_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian")
        assert person.__repr__() == "Christian"

    def test_person_representation_birth_date_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian", birth_date=date(1984, 1, 17))
        assert person.__repr__() == "Christian, born 1984-01-17"

    def test_person_representation_nationality_case(self):
        """
        GIVEN a Person model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        person = Person("Christian", nationality="Switzerland")
        assert person.__repr__() == "Christian from Switzerland"


class TestCoachClass:
    def test_new_coach_simple_case(self):
        """
        GIVEN a Coach model
        WHEN a new Coach is created
        THEN check the hash fields are defined correctly."""
        coach = Coach("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert coach.name == "Christian"
        assert coach.surname == "Pala"
        assert coach.birth_date == date(1984, 1, 17)
        assert coach.nationality == "Switzerland"

    def test_new_coach_blank_case(self):
        """
        GIVEN a Coach model
        WHEN a new Coach is created wit the minimum number of attributes required
        THEN check the hash fields are defined correctly."""
        coach = Coach("Christian")
        assert coach.name == "Christian"
        assert coach.surname is None
        assert coach.birth_date is None
        assert coach.nationality is None

    def test_new_coach_should_fail_case(self):
        """
        GIVEN a Coach model
        WHEN a new Coach is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            coach = Coach()

    def test_coach_representation_simple_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert coach.__repr__() == "Coach Christian Pala, born 1984-01-17 from Switzerland."

    def test_coach_representation_blank_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian")
        assert coach.__repr__() == "Coach Christian."

    def test_coach_representation_birth_date_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", birth_date=date(1984, 1, 17))
        assert coach.__repr__() == "Coach Christian, born 1984-01-17."

    def test_coach_representation_nationality_case(self):
        """
        GIVEN a Coach model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Coach("Christian", nationality="Switzerland")
        assert coach.__repr__() == "Coach Christian from Switzerland."


class TestPlayerClass:
    def test_new_player_simple_case(self):
        """
        GIVEN a Player model
        WHEN a new Player is created
        THEN check the hash fields are defined correctly."""
        player = Player("Christian", "FW", "Pala", date(1984, 1, 17), "Switzerland", "187 cm")
        assert player.name == "Christian"
        assert player.role == "FW"
        assert player.surname == "Pala"
        assert player.birth_date == date(1984, 1, 17)
        assert player.nationality == "Switzerland"
        assert player.height == "187 cm"

    def test_new_player_blank_case(self):
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

    def test_new_player_should_fail_case(self):
        """
        GIVEN a Player model
        WHEN a new Player is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            player = Player("Christian")

    def test_new_player_should_fail_case_2(self):
        """
        GIVEN a Player model
        WHEN a new Player is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            player = Player(role="FW")

    def test_new_player_should_fail_case_3(self):
        """
        GIVEN a Player model
        WHEN a new Player is created without the correct attributes
        THEN check it raises a TypeError."""
        with pytest.raises(TypeError):
            player = Player()

    def test_player_representation_simple_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", "Pala", date(1984, 1, 17), "Switzerland", "187 cm")
        assert player.__repr__() == "Player Christian Pala, born 1984-01-17 from Switzerland is 187 cm tall, " \
                                    "playing as forward."

    def test_player_representation_blank_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW")
        assert player.__repr__() == "Player Christian, playing as forward."

    def test_player_representation_birth_date_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        player = Player("Christian", "FW", birth_date=date(1984, 1, 17))
        assert player.__repr__() == "Player Christian, born 1984-01-17, playing as forward."

    def test_player_representation_nationality_case(self):
        """
        GIVEN a Player model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        coach = Player("Christian", "FW", nationality="Switzerland")
        assert coach.__repr__() == "Player Christian from Switzerland, playing as forward."


class TestRefereeClass:
    def test_new_referee_simple_case(self):
        """
        GIVEN a Referee model
        WHEN a new Referee is created
        THEN check the hash fields are defined correctly-"""
        referee = Referee("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert referee.name == "Christian"
        assert referee.surname == "Pala"
        assert referee.birth_date == date(1984, 1, 17)
        assert referee.nationality == "Switzerland"

    def test_new_referee_blank_case(self):
        """
        GIVEN a Referee model
        WHEN a new Referee is created with the minimum number of attributes required
        THEN check it raises a TypeError."""
        referee = Referee("Christian")
        assert referee.name == "Christian"
        assert referee.surname is None
        assert referee.birth_date is None
        assert referee.nationality is None

    def test_new_referee_should_fail_case(self):
        """
        GIVEN a Referee model
        WHEN a new Referee is created
        THEN check the hash fields are defined correctly"""
        with pytest.raises(TypeError):
            referee = Referee()

    def test_referee_representation_simple_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", "Pala", date(1984, 1, 17), "Switzerland")
        assert referee.__repr__() == "Referee Christian Pala, born 1984-01-17 from Switzerland."

    def test_referee_representation_blank_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian")
        assert referee.__repr__() == "Referee Christian."

    def test_referee_representation_birth_date_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", birth_date=date(1984, 1, 17))
        assert referee.__repr__() == "Referee Christian, born 1984-01-17."

    def test_referee_representation_nationality_case(self):
        """
        GIVEN a Referee model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        referee = Referee("Christian", nationality="Switzerland")
        assert referee.__repr__() == "Referee Christian from Switzerland."


class TestTeamClass:

    def test_new_team_simple_case(self):
        """
        GIVEN a Team model
        WHEN a new Team is created
        THEN check the hash fields are defined correctly-"""
        team = Team("Arsenal FC", "Baker Street 13, London.", "Old Trafford", "www.arsenal.co.uk")
        assert team.name == "Arsenal FC"
        assert team.address == "Baker Street 13, London."
        assert team.stadium == "Old Trafford"
        assert team.url == "www.arsenal.co.uk"

    def test_new_team_blank_case(self):
        """
        GIVEN a Team model
        WHEN a new Team is created
        THEN check the hash fields are defined correctly-"""
        team = Team("Arsenal FC", "Baker Street 13, London")
        assert team.name == "Arsenal FC"
        assert team.address == "Baker Street 13, London"
        assert team.stadium is None
        assert team.url is None

    def test_new_team_should_fail_case(self):
        """
        GIVEN a Team model
        WHEN a new Team is created
        THEN check the hash fields are defined correctly"""
        with pytest.raises(TypeError):
            team = Team()

    def test_team_representation_simple_case(self):
        """
        GIVEN a Team model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London", "Old Trafford", "www.arsenal.co.uk")
        assert team.__repr__() == "Team Arsenal FC, located: Baker Street 13, London playing at Old Trafford, " \
                                  "whose web page is: www.arsenal.co.uk."

    def test_team_representation_blank_case(self):
        """
        GIVEN a Team model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        team = Team("Arsenal FC", "Baker Street 13, London")
        assert team.__repr__() == "Team Arsenal FC, located: Baker Street 13, London."


class TestMatchClass:

    def test_new_match_simple_case(self):
        """
        GIVEN a Match model
        WHEN a new Match is created
        THEN check the hash fields are defined correctly-"""
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22), "1-0")
        assert match.home == "Arsenal FC"
        assert match.away == "Chelsea"
        assert match.day == date(1995, 3, 15)
        assert match.result == "1-0"

    def test_new_match_blank_case(self):
        """
        GIVEN a Match model
        WHEN a new Match is created
        THEN check the hash fields are defined correctly-"""
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22))
        assert match.home == "Arsenal FC"
        assert match.away == "Chelsea"
        assert match.day == date(1995, 3, 15)
        assert match.result is None

    def test_new_match_should_fail_case(self):
        """
        GIVEN a Match model
        WHEN a new Match is created
        THEN check the hash fields are defined correctly"""
        with pytest.raises(TypeError):
            match = Match()

    def test_match_representation_simple_case(self):
        """
        GIVEN a Match model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22), "1-0")
        assert match.__repr__() == "Match between Arsenal FC and Chelsea, played on the 1995-03-15 with a score of 1-0" \
                                   " during the season 2021 - 2022."

    def test_match_representation_blank_case(self):
        """
        GIVEN a Match model
        WHEN the presentation method is called
        THEN check the desired string is outputted.
        """
        match = Match("Arsenal FC", "Chelsea", date(1995, 3, 15), date(2021, 8, 13), date(2022, 5, 22))
        assert match.__repr__() == "Match between Arsenal FC and Chelsea, played on the 1995-03-15 during the season" \
                                   " 2021 - 2022."