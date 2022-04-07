# Libraries:
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from typing import List, Union, Optional
from datasets.players.player_scraper import season_generator


URL = "https://www.worldfootball.net/all_matches/eng-premier-league-"
# source for the data scraping on premier league football players

# functions:
def url_generator(seasons: str) -> str:
    """given a set of two years, generates the appropriate url for the scraper."""
    # Note: seasons must be a string like 20xx-20x(x+1), for instance 2021-2022.
    return URL + seasons + "/"

def table_scraper(container: List, url: str) -> Union[Optional[str]]:
    """ function to scrape the table of interest and save the data in a list."""
    page = requests.get(url)
    try:
        page.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)

    soup = bs(page.text, "html.parser")
    table_body = soup.find('table', attrs={'class': 'standard_tabelle'})  # the attribute is specific to this table.

    for row in table_body.find_all('tr'):
        col = row.find_all('td')
        col = [content.text.strip() for content in col]
        container.append([ele for ele in col if ele])


def database_cleaner(input_data: List, seasons: str) -> None:
    """ function to pre-process the player data."""
    dataframe = pd.DataFrame(input_data, columns=['date', 'home', 'dash', 'away', 'result','q1'])
    dataframe.dropna(how='all', inplace=True)
    filename = 'matches_' + seasons + '_clean.csv'
    dataframe.to_csv(filename, index=False)


def main():
    season_list: List[str] = season_generator(2021, 2022)
    # Note: a large number of seasons may cause a timeout error!
    for season in season_list:
        scraped_table = []
        url = url_generator(season)
        table_scraper(container=scraped_table, url=url)
        database_cleaner(scraped_table, season)


if __name__ == "__main__":
    main()
