from pl_client.services.people.coach_service import CoachService
from pl_client.services.people.referee_service import RefereeService
from pl_client.services.people.player_service import PlayerService
from pl_client.services.team_service import TeamService
from pl_client.services.match_service import MatchService
from pl_client.models.people.coach import Coach
from pl_client.models.people.referee import Referee
from pl_client.models.people.player import Player
from pl_client.models.team import Team
from pl_client.models.match_model import Match
from datetime import date


class TestCoachService:
    def test_coach_get_all(self):
        coach1 = Coach(name="Adam", surname="Sadler", nationality="England")
        coach2 = Coach(name="Aitor", surname="Karanka", nationality="Spain")
        query_coaches = CoachService.get_all()
        assert query_coaches[0].name == coach1.name
        assert query_coaches[0].surname == coach1.surname
        assert query_coaches[0].nationality == coach1.nationality
        assert query_coaches[0].birth_date == coach1.birth_date
        assert query_coaches[1].name == coach2.name
        assert query_coaches[1].surname == coach2.surname
        assert query_coaches[1].nationality == coach2.nationality
        assert query_coaches[1].birth_date == coach2.birth_date

    def test_coach_get_full_case(self):
        coach = Coach(name="Adam", surname="Sadler", nationality="England")
        query_coach = CoachService.get_item_by_id(2)
        assert query_coach.name == coach.name
        assert query_coach.surname == coach.surname
        assert query_coach.nationality == coach.nationality
        assert query_coach.birth_date == coach.birth_date

    def test_coach_get_blank_case(self):
        coach = Coach(name="Adam")
        query_coach = CoachService.get_item_by_id(2)
        assert query_coach.name == coach.name

    def test_coach_search_full_case(self):
        coach = Coach(name="Adam", surname="Sadler", nationality="England")
        query_coaches = CoachService.search_items(name="Adam", surname="Sadler", nationality="England")
        assert query_coaches[0].name == coach.name
        assert query_coaches[0].surname == coach.surname
        assert query_coaches[0].nationality == coach.nationality
        assert query_coaches[0].birth_date == coach.birth_date

    def test_coach_search_blank_case(self):
        coach = Coach(name="Adam")
        query_coaches = CoachService.search_items(surname="Sadler")
        assert query_coaches[0].name == coach.name

    def test_coach_search_not_found(self):
        query_coaches = CoachService.search_items(nationality='Japan')
        assert len(query_coaches) == 0

    def test_coach_add_blank(self):
        coach_to_add = Coach(name="Christian")
        status_code = CoachService.add_item(coach_to_add)
        assert status_code == 200

    def test_coach_add_full(self):
        coach_to_add = Coach(name="Christian", surname="Pala", nationality="Switzerland")
        status_code = CoachService.add_item(coach_to_add)
        assert status_code == 200

    def test_coach_update_blank(self):
        coach_to_update = Coach(name="Adam")
        status_code = CoachService.update_item_by_id(274, coach_to_update)
        assert status_code == 200

    def test_coach_update_full(self):
        coach_to_update = Coach(name="Adam", surname="Sadler", nationality="England")
        status_code = CoachService.update_item_by_id(275, coach_to_update)
        assert status_code == 200

    def test_coach_delete(self):
        status_code = CoachService.delete_item_by_id(549)
        assert status_code == 200

    def test_coach_find_ids(self):
        coach_id = CoachService.find_ids(name="Adam")
        assert coach_id[0]['id'] == 2


class TestRefereeService:
    def test_referee_get_all(self):
        referee1 = Referee(name="Alan",
                           surname="Wilkie",
                           nationality="England")
        referee2 = Referee(name="Allan",
                           surname="Gunn",
                           nationality="England")
        query_referees = RefereeService.get_all()
        assert query_referees[0].name == referee1.name
        assert query_referees[0].surname == referee1.surname
        assert query_referees[0].nationality == referee1.nationality
        assert query_referees[1].name == referee2.name
        assert query_referees[1].surname == referee2.surname
        assert query_referees[1].nationality == referee2.nationality

    def test_referee_get_full_case(self):
        referee = Referee(name="Alan",
                          surname="Wilkie",
                          birth_date=None,
                          nationality="England")
        query_referee = RefereeService.get_item_by_id(2)
        assert query_referee.name == referee.name
        assert query_referee.surname == referee.surname
        assert query_referee.nationality == referee.nationality
        assert query_referee.birth_date == referee.birth_date

    def test_referee_get_blank_case(self):
        referee = Referee(name="Alan")
        query_referee = RefereeService.get_item_by_id(2)
        assert query_referee.name == referee.name

    def test_referee_search_full_case(self):
        referee = Referee(name="Allan",
                          surname="Gunn",
                          birth_date=date(1943, 1, 23),
                          nationality="England")
        query_referees = RefereeService.search_items(name="Allan",
                                                     surname="Gunn",
                                                     nationality="England")
        assert query_referees[0].name == referee.name
        assert query_referees[0].surname == referee.surname
        assert query_referees[0].nationality == referee.nationality
        assert query_referees[0].birth_date == referee.birth_date

    def test_referee_search_surname_case(self):
        referee = Referee(name="Alan")
        query_referees = RefereeService.search_items(surname="Wilkie")
        assert query_referees[0].name == referee.name

    def test_referee_search_birth_date_case(self):
        referee = Referee(name="Allan")
        query_referees = RefereeService.search_items(birth_date=date(1943, 1, 23))
        assert query_referees[0].name == referee.name

    def test_referee_search_nationality_case(self):
        referee = Referee(name="Jarred")
        query_referees = RefereeService.search_items(nationality='Australia')
        assert query_referees[0].name == referee.name

    def test_referee_search_not_found(self):
        query_referees = RefereeService.search_items(nationality='Japan')
        assert len(query_referees) == 0

    def test_referee_add_blank(self):
        referee_to_add = Referee(name="Carlo")
        query_referees = RefereeService.search_items(name="Carlo")
        assert len(query_referees) == 0
        status_code = RefereeService.add_item(referee_to_add)
        assert status_code == 200
        query_referees_2 = RefereeService.search_items(name="Carlo")
        assert query_referees_2[0].name == referee_to_add.name

    def test_referee_add_full(self):
        referee_to_add = Referee(name="Christian", surname="Pala", birth_date=date(1971, 7, 14))
        query_referees = RefereeService.search_items(name="Christian", surname="Pala", birth_date=date(1971, 7, 14))
        assert len(query_referees) == 0
        status_code = RefereeService.add_item(referee_to_add)
        assert status_code == 200
        query_referees_2 = RefereeService.search_items(name="Christian", surname="Pala", birth_date=date(1971, 7, 14))
        assert query_referees_2[0].name == referee_to_add.name

    def test_referee_update_full(self):
        referee_to_update = Referee(name="Adam", surname="Sadler", birth_date=date(1900, 1, 1), nationality="England")
        status_code = RefereeService.update_item_by_id(59, referee_to_update)
        assert status_code == 200

    def test_referee_update_empty(self):
        referee_to_update = Referee(name="Adam")
        status_code = RefereeService.update_item_by_id(89, referee_to_update)
        assert status_code == 200

    def test_referee_delete(self):
        status_code = RefereeService.delete_item_by_id(93)
        assert status_code == 200

    def test_referee_find_ids(self):
        referee_id = RefereeService.find_ids("Allan")
        assert referee_id[0]['id'] == 3


class TestPlayerService:
    def test_player_get_all(self):
        player1 = Player(name="Christian",
                         role="GK",
                         surname="Pala",
                         birth_date=date(2001, 5, 28),
                         nationality="Switzerland",
                         height=180)
        player2 = Player(name="Alexis",
                         role="FW",
                         surname="Ronaldo",
                         birth_date=date(1985, 1, 1),
                         nationality="Portugal",
                         height=180)
        query_players = PlayerService.get_all()
        assert query_players[0].name == player1.name
        assert query_players[0].surname == player1.surname
        assert query_players[0].nationality == player1.nationality
        assert query_players[0].birth_date == player1.birth_date
        assert query_players[1].name == player2.name
        assert query_players[1].surname == player2.surname
        assert query_players[1].nationality == player2.nationality
        assert query_players[1].birth_date == player2.birth_date

    def test_player_get_full_case(self):
        player = Player(name="Cristiano",
                        role="FW",
                        surname="Ronaldo",
                        birth_date=date(1985, 1, 1),
                        nationality="Portugal",
                        height=180)
        query_player = PlayerService.get_item_by_id(13)
        assert query_player.name == player.name
        assert query_player.surname == player.surname
        assert query_player.nationality == player.nationality
        assert query_player.birth_date == player.birth_date
        assert query_player.role == player.role
        assert query_player.height == player.height

    def test_player_get_blank_case(self):
        player = Player(name="Christian", role="GK")
        query_player = PlayerService.get_item_by_id(8)
        assert query_player.name == player.name

    def test_player_search_full_case(self):
        player = Player(name="Cristiano",
                        role="FW",
                        surname="Ronaldo",
                        birth_date=date(1985, 1, 1),
                        nationality="Portugal",
                        height=180)
        query_players = PlayerService.search_items(name="Cristiano",
                                                   role="FW",
                                                   surname="Ronaldo",
                                                   birth_date=date(1985, 1, 1),
                                                   nationality="Portugal",
                                                   height=180)
        assert query_players[0].name == player.name
        assert query_players[0].surname == player.surname
        assert query_players[0].nationality == player.nationality
        assert query_players[0].birth_date == player.birth_date

    def test_player_search_surname_case(self):
        player = Player(name="Christian", role="GK")
        query_players = PlayerService.search_items(surname="Pala")
        assert query_players[0].name == player.name

    def test_player_search_birth_date_case(self):
        player = Player(name="Christian", role="GK")
        query_players = PlayerService.search_items(birth_date=date(2001, 5, 28))
        assert query_players[0].name == player.name

    def test_player_search_nationality_case(self):
        player = Player(name="Christian", role="GK")
        query_players = PlayerService.search_items(nationality="Switzerland")
        assert query_players[0].name == player.name

    def test_player_search_not_found(self):
        player = Player(name="Carlo", role="GK")
        query_players = PlayerService.search_items(nationality="Japan")
        assert len(query_players) == 0

    def test_player_add_blank(self):
        player_to_add = Player(name="Mark", role="FW")
        query_players = PlayerService.search_items(name="Mark", role="FW")
        assert len(query_players) == 0
        status_code = PlayerService.add_item(player_to_add)
        assert status_code == 200
        query_players_2 = PlayerService.search_items(name="Mark", role="FW")
        assert query_players_2[0].name == player_to_add.name

    def test_player_add_full(self):
        player_to_add = Player(name="Paul", role="MF", surname="Pogba", birth_date=date(1986, 1, 1),
                               nationality="France", height=180)
        query_players = PlayerService.search_items(name="Paul")
        assert len(query_players) == 0
        status_code = PlayerService.add_item(player_to_add)
        assert status_code == 200
        query_players_2 = PlayerService.search_items(name="Paul")
        assert query_players_2[0].name == player_to_add.name

    def test_player_update_full(self):
        player_to_update = Player(name="Lionel", role="FW", surname="Messi", birth_date=date(1990, 1, 1),
                                  nationality="Argentina", height=160)
        status_code = PlayerService.update_item_by_id(99, player_to_update)
        assert status_code == 200

    def test_player_update_empty(self):
        player_to_update = Player(name="Romelu", role="FW")
        status_code = PlayerService.update_item_by_id(50, player_to_update)
        assert status_code == 200

    def test_player_delete(self):
        status_code = PlayerService.delete_item_by_id(9)
        assert status_code == 200

    def test_player_find_ids(self):
        player_id = PlayerService.find_ids(name="Cristiano")
        assert player_id[0]['id'] == 13


class TestTeamService:
    def test_team_get_all(self):
        team1 = Team(name="AFC Bournemouth",
                     address="Dean Court Ground - Bournemouth",
                     stadium="Vitality Stadium",
                     url="https://www.afcb.co.uk/")
        team2 = Team(name="Arsenal FC",
                     address="Drayton Park 75 - Highbury - N5 1BU London",
                     stadium="Emirates Stadium",
                     url="https://www.arsenal.com/")
        query_teams = TeamService.get_all()
        assert query_teams[0].name == team1.name
        assert query_teams[0].address == team1.address
        assert query_teams[0].stadium == team1.stadium
        assert query_teams[0].url == team1.url
        assert query_teams[1].name == team2.name
        assert query_teams[1].address == team2.address
        assert query_teams[1].stadium == team2.stadium
        assert query_teams[1].url == team2.url

    def test_team_get_full_case(self):
        team = Team(name="AFC Bournemouth",
                     address="Dean Court Ground - Bournemouth",
                     stadium="Vitality Stadium",
                     url="https://www.afcb.co.uk/")
        query_team = TeamService.get_item_by_id(11)
        assert query_team.name == team.name
        assert query_team.address == team.address
        assert query_team.stadium == team.stadium
        assert query_team.url == team.url

    def test_team_get_blank_case(self):
        team = Team(name="AFC Bournemouth",
                    address="Dean Court Ground - Bournemouth")
        query_team = TeamService.get_item_by_id(11)
        assert query_team.name == team.name
        assert query_team.address == team.address

    def test_team_search_full_case(self):
        team = Team(name="AFC Bournemouth",
                     address="Dean Court Ground - Bournemouth",
                     stadium="Vitality Stadium",
                     url="https://www.afcb.co.uk/")
        query_teams = TeamService.search_items(name="AFC Bournemouth",
                                               address="Dean Court Ground - Bournemouth",
                                               stadium="Vitality Stadium",
                                               url="https://www.afcb.co.uk/")
        assert query_teams[0].name == team.name
        assert query_teams[0].address == team.address
        assert query_teams[0].stadium == team.stadium
        assert query_teams[0].url == team.url

    def test_team_search_address_case(self):
        team = Team(name="AFC Bournemouth",
                     address="Dean Court Ground - Bournemouth",
                     stadium="Vitality Stadium",
                     url="https://www.afcb.co.uk/")
        query_teams = TeamService.search_items(address="Dean Court Ground - Bournemouth")
        assert query_teams[0].name == team.name

    def test_team_search_stadium_case(self):
        team = Team(name="AFC Bournemouth",
                     address="Dean Court Ground - Bournemouth",
                     stadium="Vitality Stadium",
                     url="https://www.afcb.co.uk/")
        query_teams = TeamService.search_items(stadium="Vitality Stadium")
        assert query_teams[0].name == team.name

    def test_team_search_url_case(self):
        team = Team(name="AFC Bournemouth",
                     address="Dean Court Ground - Bournemouth",
                     stadium="Vitality Stadium",
                     url="https://www.afcb.co.uk/")
        query_teams = TeamService.search_items(url="https://www.afcb.co.uk/")
        assert query_teams[0].name == team.name

    def test_team_search_not_found(self):
        query_teams = TeamService.search_items(stadium="Japan")
        assert len(query_teams) == 0

    def test_team_add_blank(self):
        team_to_add = Team(name="AC Milan", address="Milano")
        query_teams = TeamService.search_items(name="AC Milan", address="Milano")
        assert len(query_teams) == 0
        status_code = TeamService.add_item(team_to_add)
        assert status_code == 200
        query_teams_2 = TeamService.search_items(name="AC Milan", address="Milano")
        assert query_teams_2[0].name == team_to_add.name

    def test_team_add_full(self):
        team_to_add = Team(name="Juventus FC", address="Turin", stadium="Allianz Stadium", url="www.juventus.it")
        query_teams = TeamService.search_items(name="Juventus FC", address="Turin")
        assert len(query_teams) == 0
        status_code = TeamService.add_item(team_to_add)
        assert status_code == 200
        query_teams_2 = TeamService.search_items(name="Juventus FC", address="Turin")
        assert query_teams_2[0].name == team_to_add.name

    def test_team_update_full(self):
        team_to_update = Team(name="Juventus FC", address="Turin", stadium="Allianz Stadium", url="www.juventus.it")
        status_code = TeamService.update_item_by_id(15, team_to_update)
        assert status_code == 200

    def test_player_update_empty(self):
        team_to_update = Team(name="Juventus FC", address="Turin")
        status_code = TeamService.update_item_by_id(16, team_to_update)
        assert status_code == 200

    def test_team_delete(self):
        status_code = TeamService.delete_item_by_id(33)
        assert status_code == 200

    def test_team_find_ids(self):
        team_id = TeamService.find_ids(name="Arsenal FC")
        assert team_id[0]['id'] == 12



class TestMatchService:
    def test_match_get_all(self):
        match1 = Match("Arsenal", "Brentford", date(2022, 1, 1), date(1985, 1, 1), date(1986, 1, 1), "1:2")
        match2 = Match("Arsenal", "Brentford", date(2022, 1, 1), date(1985, 1, 1), date(1986, 1, 1), "3:0")
        query_matches = MatchService.get_all()
        assert query_matches[0].home == match1.home
        assert query_matches[0].away == match1.away
        assert query_matches[0].day == match1.day
        assert query_matches[0].season_start == match1.season_start
        assert query_matches[0].season_end == match1.season_end
        assert query_matches[0].result == match1.result
        assert query_matches[1].home == match2.home
        assert query_matches[1].away == match2.away
        assert query_matches[1].day == match2.day
        assert query_matches[1].season_start == match2.season_start
        assert query_matches[1].season_end == match2.season_end
        assert query_matches[1].result == match2.result

    def test_match_get_full_case(self):
        match = Match("Arsenal", "Brentford", date(2022, 1, 1), date(1985, 1, 1), date(1986, 1, 1), "1:2")
        query_match = MatchService.get_item_by_id(3)
        assert query_match.home == match.home
        assert query_match.away == match.away
        assert query_match.day == match.day
        assert query_match.season_start == match.season_start
        assert query_match.season_end == match.season_end
        assert query_match.result == match.result

    def test_match_get_blank_case(self):
        match = Match("Arsenal", "Brentford", date(2022, 1, 1), date(1985, 1, 1), date(1986, 1, 1), "1:2")
        query_match = MatchService.get_item_by_id(3)
        assert query_match.home == match.home
        assert query_match.away == match.away

    def test_match_search_full_case(self):
        match = Match("Arsenal", "Brentford", date(2022, 1, 1), date(1985, 1, 1), date(1986, 1, 1), "1:2")
        query_matches = MatchService.search_items("Arsenal", "Brentford", date(2022, 1, 1), date(1985, 1, 1), date(1986, 1, 1), "1:2")
        assert query_matches[0].home == match.home
        assert query_matches[0].away == match.away

    def test_match_search_day_case(self):
        match = Match("Arsenal", "Brentford", date(2022, 1, 1), date(1985, 1, 1), date(1986, 1, 1), "1:2")
        query_matches = MatchService.search_items(day=date(2022, 1, 1))
        assert query_matches[0].home == match.home
        assert query_matches[0].away == match.away

    def test_match_search_not_found(self):
        query_matches = MatchService.search_items(home="Real Madrid")
        assert len(query_matches) == 0
        
    def test_match_add_blank(self):
        match_to_add = Match("Brentford", "Chelsea", date(2022, 1, 23), date(2021, 8, 13), date(2022, 5, 22))
        query_matches = MatchService.search_items(home="Brentford", away="Chelsea")
        assert len(query_matches) == 0
        status_code = MatchService.add_item(match_to_add)
        assert status_code == 200
        query_matches_2 = MatchService.search_items(home="Brentford", away="Chelsea")
        assert query_matches_2[0].home == match_to_add.home

    def test_match_add_full(self):
        match_to_add = Match("Brentford_FC", "Chelsea_FC", date(2022, 1, 23), date(2021, 8, 13), date(2022, 5, 22),
                             "2:0")
        query_matches = MatchService.search_items(home="Brentford_FC", away="Chelsea_FC")
        assert len(query_matches) == 0
        status_code = MatchService.add_item(match_to_add)
        assert status_code == 200
        query_matches_2 = MatchService.search_items(home="Brentford_FC", away="Chelsea_FC")
        assert query_matches_2[0].home == match_to_add.home

    def test_match_update_full(self):
        match_to_update = Match(home="Arsenal", away="Brentford", day=date(2022, 1, 1),
                                season_start=date(1985, 1, 1), season_end=date(1986, 1, 1), result="2:0")
        status_code = MatchService.update_item_by_id(30, match_to_update)
        assert status_code == 200

    def test_match_update_blank(self):
        match_to_update = Match(home="Arsenal", away="Brentford", day=date(2022, 1, 1),
                                season_start=date(1985, 1, 1), season_end=date(1986, 1, 1))
        status_code = MatchService.update_item_by_id(31, match_to_update)
        assert status_code == 200

    def test_match_delete(self):
        status_code = MatchService.delete_item_by_id(211)
        assert status_code == 200

    def test_match_find_ids(self):
        match_id = MatchService.find_ids(home="Arsenal", away='Brentford', day=date(2022, 1, 1))
        assert match_id[0]['id'] == 3
