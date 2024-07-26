#    Copyright 2024 Sakan Nirattisaykul
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import sqlite3
from sqlite3 import OperationalError

import pandas as pd
from loguru import logger


def insert_to_sqlite(db: str, data: pd.DataFrame, table_name: str) -> None:
    """
    Insert data into the SQLite database.
    :param db: SQLite database path.
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
        'primary_stress_position': 'Text',
        'secondary_stress_position': 'Text'
    }

    try:
        with sqlite3.connect(db) as conn:
            data.to_sql(table_name, conn, if_exists='replace', index=False, dtype=dtype_dict)
            conn.commit()
        logger.info('Inserted data successfully.')
    except OperationalError as e:
        logger.error(f'Database connection error: {e}')
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    pass
