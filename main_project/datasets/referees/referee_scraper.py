# Libraries:
import pandas as pd
from datasets.utils.utility_functions import season_generator, url_generator, table_scraper
from typing import List

URL = "https://www.worldfootball.net/referees/eng-premier-league-"
# source for the data scraping on premier league football players

# functions:


def referee_database_cleaner(input_data: List, seasons: str) -> None:
    """ function to pre-process the player data."""
    print(input_data)
    dataframe = pd.DataFrame(input_data, columns=['referee', 'born', 'nationality', 'g1', 'g2', 'g3', 'g4'])
    dataframe.dropna(how='all', inplace=True)
    dataframe = dataframe.iloc[:-1, 0:3]
    dataframe.rename(columns={'born': 'birth_date'}, inplace=True)
    dataframe[['name', 'surname']] = dataframe['referee'].str.split(' ', 1, expand=True)
    dataframe.drop(columns=['referee'], axis=1, inplace=True)
    dataframe = dataframe.reindex(columns=['name', 'surname', 'birth_date', 'nationality'])
    filename = 'referee_' + seasons + '_clean.csv'
    dataframe.to_csv(filename, index=False)


def main():
    season_list: List[str] = season_generator(2021, 2022)
    # Note: a large number of seasons may cause a timeout error!
    for season in season_list:
        scraped_table = []
        url = url_generator(URL, season, '/1')
        table_scraper(container=scraped_table, url=url, table_name="standard_tabelle")
        referee_database_cleaner(scraped_table, season)


if __name__ == "__main__":
    main()


