import sqlite3

import pytest

from stress_pattern_finder.eng_stress_pattern_finder import find_stress_pattern
from stress_pattern_finder.stress_pattern_etl.load_to_sqlite import insert_to_sqlite


def test_full_process():
    data_path = 'SUBTLEXus74286wordstextversion.tsv'
    dataframe = find_stress_pattern(data_path)
    db = 'test_full_process.db'
    insert_to_sqlite(db, dataframe, 'StressPattern')

    assert not dataframe.empty

    # Check columns
    assert dataframe.shape[1] == 13

    # Check whether data is loaded properly
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM StressPattern')
        rows = cursor.fetchall()
        assert len(rows) > 0

        cursor.execute('SELECT * FROM SyllableGroup')
        rows = cursor.fetchall()
        assert len(rows) > 0


if __name__ == '__main__':
    pytest.main([__file__])
