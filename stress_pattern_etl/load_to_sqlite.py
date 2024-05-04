import os
import sqlite3

import pandas as pd
from loguru import logger
from sqlalchemy import create_engine


class LoadToSqlite:
    def __init__(self):
        """
        Initialize the SQLite database if not exist.
        """
        logger.info("Initializing SQLite database...")
        self.database = 'eng_stress_pattern.db'
        self.sqlalchemy_engine = create_engine(f'sqlite:///{self.database}')

        if os.path.exists(self.database):
            logger.info(f"SQLite database '{self.database}' already exists.")
        else:
            logger.info(f"Initializing SQLite database '{self.database}'...")

    def insert_to_sqlite(self, data: pd.DataFrame, table_name: str) -> None:
        """
        Insert data into the SQLite database.
        :param data: Pandas dataframe containing data to be inserted.
        :param table_name: Table name
        :return: None
        """
        logger.info('Inserting data to database...')

        dtype_dict = {
            'Word': 'Text',
            'FREQcount': 'Integer',
            'CDcount': 'Integer',
            'FREQlow': 'Integer',
            'Cdlow': 'Integer',
            'SUBTLWF': 'Float',
            'Lg10WF': 'Float',
            'SUBTLCD': 'Float',
            'Lg10CD': 'Float',
            'syllable_count': 'Integer',
            'stress_pattern': 'Text',
            'primary_stress_position': 'Integer',
            'secondary_stress_position': 'Integer'
        }

        try:
            with sqlite3.connect(self.database) as conn:
                data.to_sql(table_name, conn, if_exists='replace', index=False, dtype=dtype_dict)
                conn.commit()
            logger.info('Inserted data successfully.')
        except Exception as e:
            logger.error(e)
            logger.error('Failed to insert data to database.')


if __name__ == '__main__':
    pass
