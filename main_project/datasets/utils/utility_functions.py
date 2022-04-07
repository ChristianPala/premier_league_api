import csv
import pandas as pd
# from flask_sqlalchemy import SQLAlchemy
# from app import create_app
import requests
from bs4 import BeautifulSoup as bs
from typing import List, Union

# commented in case of circular imports, not required after first database population

# db = SQLAlchemy(create_app())


def populate_table(table_name: str, filename: csv, date_field_name: str = None, chunk_size: int = 500) -> None:
    """ auxiliary method to populate a mysql table with sql_alchemy"""
    df = pd.read_csv(filename)
    if date_field_name is not None:
        df[date_field_name] = pd.to_datetime(df[date_field_name], errors='coerce')
    df.to_sql(table_name, con=db.engine, if_exists='append', index=False, chunksize=chunk_size)


def url_generator(url: str, seasons: str, sort: str = None) -> str:
    """given a set of two years, generates the appropriate url for the scraper for the website
        worldfootball.net"""
    # Note: seasons must be a string like 20xx-20x(x+1), for instance 2021-2022.
    return ''.join(filter(None, (url, seasons, sort)))


def season_generator(first_season: int, last_season: int) -> List[str]:
    """Creates a list comprising the seasons of interest for a given period of years from the current year."""
    period = last_season - first_season
    season_list: List[str] = [str(last_season - i - 1) + '-' + str(last_season - i) for i in range(period)]
    return season_list


def table_scraper(container: List, url: str, table_name: str) -> Union[str, None]:
    """ function to scrape the table of interest and save the data in a list."""
    page = requests.get(url)
    try:
        page.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)

    soup = bs(page.text, "html.parser")
    table_body = soup.find('table', attrs={'class': table_name})  # the attribute is specific to this table.

    for row in table_body.find_all('tr'):
        col = row.find_all('td')
        col = [content.text.strip() for content in col]
        container.append([ele for ele in col if ele])
