import pandas as pd
from loguru import logger

from stress_pattern_etl.extract_and_transform_syllable_data import TransformSyllableData
from stress_pattern_etl.load_to_sqlite import LoadToSqlite

logger.add(
    'extract_stress_pattern.log',
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name} | {module} | {function} | {line} | {message}",
    mode='w'
)


def run_etl_process(data_path: str) -> None:
    """
    Execute an ETL process.

    - Extract the syllable data from the dataset.

    - Transform the syllable data.

    - Load the data into SQLite database.
    :param data_path: Dataset path
    :return: None
    """
    logger.info('Starting ETL process...')
    logger.info(f'Extract syllable data from {data_path}')
    dataset = pd.read_csv(data_path, delimiter='\t')
    TransformSyllableData().apply_count_syllable(dataset)

    dataset = TransformSyllableData().transform_syllable_data()

    LoadToSqlite().insert_to_sqlite(dataset, 'StressPattern')


if __name__ == '__main__':
    data_path = 'SUBTLEXus74286wordstextversion.tsv'
    run_etl_process(data_path)
