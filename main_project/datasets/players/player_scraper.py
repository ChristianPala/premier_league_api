# Libraries:
import pandas as pd
import requests
from datasets.utils.utility_functions import season_generator, url_generator
from bs4 import BeautifulSoup as bs
from typing import List, Union, Optional

URL = "https://www.worldfootball.net/players_list/eng-premier-league-"
# source for the data scraping on premier league football players
SORT = "/nach-name/"
# in order to have the table sorted alphabetically.
PAGES = 14
# maximum length of the table as of 2022.


# functions:

def player_table_scraper(n_pages: int, container: List, url: str) -> Union[Optional[str]]:
    """ function to scrape the table of interest and save the data in a list."""
    for i in range(1, n_pages + 1):
        page_url: str = url + str(i) + '/'
        page = requests.get(page_url)
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


def player_database_cleaner(input_data: List, seasons: str) -> None:
    """ function to pre-process the player data."""
    dataframe = pd.DataFrame(input_data, columns=['player', 'team', 'born', 'height', 'Position'])
    dataframe.rename(columns={'born': 'birth_date', 'Position': 'role'}, inplace=True)
    dataframe = dataframe.iloc[1:, :]
    dataframe[['name', 'surname']] = dataframe['player'].str.split(' ', 1, expand=True)
    dataframe.drop(columns=['team', 'player'], axis=1, inplace=True)
    dataframe = dataframe.reindex(columns=['name', 'surname', 'birth_date', 'height', 'role'])
    filename = 'players_' + seasons + '_clean.csv'
    dataframe.to_csv(filename, index=False)


def main():
    season_list: List[str] = season_generator(2020, 2021)
    # Note: a large number of seasons may cause a timeout error!
    for season in season_list:
        scraped_table = []
        url = url_generator(URL, season, SORT)
        player_table_scraper(n_pages=PAGES, container=scraped_table, url=url)
        player_database_cleaner(input_data=scraped_table, seasons=season)


if __name__ == "__main__":
    main()


