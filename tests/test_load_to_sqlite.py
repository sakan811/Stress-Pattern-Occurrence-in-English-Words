import sqlite3

import pandas as pd
import pytest

from stress_pattern_etl import LoadToSqlite


def test_insert_data_successfully():
    # Given
    load_to_sqlite = LoadToSqlite()
    data = pd.DataFrame({'Word': ['apple', 'banana', 'cherry'],
                         'FREQcount': [10, 20, 30],
                         'CDcount': [5, 10, 15],
                         'FREQlow': [5, 10, 15],
                         'Cdlow': [2, 4, 6],
                         'SUBTLWF': [0.1, 0.2, 0.3],
                         'Lg10WF': [1.0, 1.3, 1.6],
                         'SUBTLCD': [0.4, 0.5, 0.6],
                         'Lg10CD': [1.9, 2.2, 2.5],
                         'syllable_count': [2, 3, 1],
                         'stress_pattern': ['01', '010', '0'],
                         'primary_stress_position': [2, 2, 0],
                         'secondary_stress_position': [0, 0, 0]})
    table_name = 'test_table'

    # When
    load_to_sqlite.insert_to_sqlite(data, table_name)

    # Then
    with sqlite3.connect(load_to_sqlite.database) as conn:
        result = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    assert result.equals(data)


if __name__ == '__main__':
    pytest.main()
