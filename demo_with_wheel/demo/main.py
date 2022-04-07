# Libraries
import streamlit as st
from PIL import Image
from streamlit.delta_generator import DeltaGenerator
from presenter import match_printer, team_printer, person_printer, player_printer

# Imports from client wheel
from pl_client.services.people.coach_service import CoachService
from pl_client.services.match_service import MatchService
from pl_client.services.people.referee_service import RefereeService
from pl_client.services.people.player_service import PlayerService
from pl_client.models.people.player import Player
from pl_client.services.team_service import TeamService

# Custom JSON type hint.
from typing import Any, Dict, List, Tuple, Type, Union
# Custom JSON type hint.
JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


# Globals:
# Fielded players source: https://www.fantasyfootballscout.co.uk/team-news/

__fielded_chelsea_players: List[str] = ["Lukaku", "Werner", "Havertz", "Mount", "Kante", "Kovacic", "Alonso",
                                        "Rudiger", "Silva", "Azpilicueta", "Revuelta"]

__fielded_tottenham_players: List[str] = ["Kane", "Moura", "Doherty", "Skipp", "Winks", "Højbjerg", "Reguilon",
                                          "Sanchez", "Dier", "Davis", "Lloris"]


# Functions:
def search_players_by_surname(player_list: List[str]) -> Tuple[List[Player], List[str]]:
    searched_players: List = list()
    problem_cases: List = list()
    for player_surname in player_list:
        try:
            if player_surname == "Silva":
                # we need the right Silva amongst many ;-).
                player: Player = PlayerService.search_items(surname=player_surname)[8]
                # we need the right Sanchez amongst a few.
            elif player_surname == "Sanchez":
                player: Player = PlayerService.search_items(surname=player_surname)[2]
            else:
                player: Player = PlayerService.search_items(surname=player_surname)[0]

            searched_players.append(player)

        except IndexError:
            problem_cases.append(player_surname)
    print(problem_cases)

    return searched_players, problem_cases


def run_demo():
    # Page Configuration
    st.set_page_config(page_title="Chelsea - Tottenham")

    header: DeltaGenerator = st.container()
    match_container: DeltaGenerator = st.container()
    formations: DeltaGenerator = st.container()
    preview: DeltaGenerator = st.container()
    prediction: DeltaGenerator = st.container()

    # ---------- Matches ----------- #
    with header:
        st.title("Chelsea - Tottenham Preview")
        st.text("By Carlo Grigioni and Christian Pala")
        st.write("---")

    with match_container:
        # search for the match to display.
        match = MatchService.search_items(home="Chelsea FC", away="Tottenham Hotspur F.C.")[0]
        # demo presentation method.
        match_printer(match)

    with formations:
        st.markdown("<h2 style='text-align: center;'>Formations</h2>", unsafe_allow_html=True)
    # ---------- Formations ----------- #
        chelsea_image_container, tottenham_image_container = st.columns(2)

        with chelsea_image_container:
            chelsea_image = Image.open("resources/images/chelsea_starting_11.png")
            st.image(chelsea_image, caption="Chelsea starting eleven")

        with tottenham_image_container:
            tottenham_image = Image.open("resources/images/tottenham_starting_11.png")
            st.image(tottenham_image, caption="Tottenham starting eleven")
        st.write("---")

    # ---------- Referee ----------- #
    with preview:

        st.subheader("Referee")

        with st.expander("See referee"):
            col1, col2 = st.columns(2)
            with col1:
                # using search by parameter to display referee
                referee = RefereeService.search_items("Andre", "Marriner")[0]
                person_printer(referee)
            with col2:
                english_flag = Image.open("resources/images/english_flag.png")
                st.image(english_flag)

        st.subheader("Teams")
        with st.expander("See teams"):
            chelsea_team_preview_container, tottenham_team_preview_container = st.columns(2)
            with chelsea_team_preview_container:
                # using get by id to display team.
                chelsea = TeamService.get_item_by_id(15)
                team_printer(chelsea)

            with tottenham_team_preview_container:
                # using get by id to display team.
                tottenham = TeamService.get_item_by_id(44)
                team_printer(tottenham)

        st.subheader("Coaches")
        with st.expander("See coaches"):
            chelsea_coach_preview_container, flag1, tottenham_coach_preview_container, flag2 = st.columns(4)

            with chelsea_coach_preview_container:
                chelsea_coach = CoachService.search_items("Thomas", "Tuchel")[0]
                person_printer(chelsea_coach)

            with flag1:
                german_flag = Image.open("resources/images/german_flag.png")
                st.image(german_flag)

            with tottenham_coach_preview_container:
                tottenham_coach = CoachService.search_items("Antonio", "Conte")[0]
                person_printer(tottenham_coach)

            with flag2:
                italian_flag = Image.open("resources/images/italian_flag.png")
                st.image(italian_flag)

        st.subheader("Starting Players")

        st.markdown("<h4 style='text-align: left;'>Chelsea</h4>", unsafe_allow_html=True)
        with st.expander("See players"):
            for player in search_players_by_surname(__fielded_chelsea_players)[0]:
                player_printer(player)

        st.markdown("<h4 style='text-align: left;'>Tottenham</h4>", unsafe_allow_html=True)
        with st.expander("See players"):
            for player in search_players_by_surname(__fielded_tottenham_players)[0]:
                player_printer(player)

    with prediction:
        st.write("---")
        # center the button
        result = st.button("Fan prediction")
        if result:
            result = "We predict 1-0 for Chelsea"  # fan result prediction, the fans being Carlo and Christian ;-).
            st.write(result)


if __name__ == '__main__':
    run_demo()
