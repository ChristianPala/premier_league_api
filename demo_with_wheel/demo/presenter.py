# Python script for how we present the classes in our demo.

# Libraries:
import streamlit as st
from pl_client.services.utils import date_to_long_string
from pl_client.models.people.person import Person


def match_printer(match) -> None:
    """
        presenter function for matches, all fields are required so no checks are needed.
    """
    st.write(f"Match date: {date_to_long_string(match.day)}")
    st.write(f"Home team: {match.home}")
    st.write(f"Away team: {match.away}")
    st.write(f"Season: {match.season_start.year} - {match.season_end.year}")
    st.write("---")


def team_printer(team) -> None:
    """
        presenter function for teams, all fields are required so no checks are needed.
    """
    st.write(f"Name: {team.name}")
    st.write(f"Address: {team.address}")
    st.write(f"Stadium: {team.stadium}")
    st.write(f"Website: {team.url}")


def person_printer(person):
    """
        presenter function for teams, all fields are required so no checks are needed.
    """
    if person.surname:
        st.write(f"Name: {person.name} {person.surname}")
    else:
        st.write(f"Name: {person.name}")

    if person.birth_date:
        st.write(f"Birthdate: {date_to_long_string(person.birth_date)}")

    if person.nationality:
        st.write(f"Country: {person.nationality}")


def player_printer(player):
    """
        presenter function for teams, all fields are required so no checks are needed.
    """
    # there is a bit of code duplication here but it seemed over engineering to create a class structure just for this.
    person_printer(player)

    if player.height:
        st.write(f"Height: {player.height}")

    # required field so no check necessary:
    st.write(f"Role: {player.role_dictionary[player.role]}")

    st.write("---")

