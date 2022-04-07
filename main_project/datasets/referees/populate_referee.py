import pandas as pd
from sqlalchemy import create_engine
from app import db_connection
from datasets.utils.utility_functions import populate_table

if __name__ == '__main__':
    populate_table('referee', 'premier_league_referees_1993_2022.csv', 'birth_date')
