import os
import pandas as pd
import nltk
from nltk.corpus import cmudict
from pandas import DataFrame
from pandas.core.groupby import DataFrameGroupBy
from loguru import logger
from load_to_sqlite import LoadToSqlite

logger.add(
    'extract_stress_pattern.log',
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name} | {module} | {function} | {line} | {message}",
    mode='w'
)

logger.info('Download the cmudict data.')
nltk.download('cmudict')
pron_dict = cmudict.dict()


def load_data(dataset_path: str) -> DataFrame:
    return pd.read_csv(dataset_path, delimiter='\t')


def save_data(data: DataFrame, output_path: str) -> None:
    data.to_csv(output_path, sep='\t', index=False)


def count_syllables(word: str):
    if isinstance(word, str):  # check if word is a string
        try:
            return [len(list(y for y in x if y[-1].isdigit())) for x in pron_dict[word.lower()]][0]
        except KeyError:
            # handle case where word is not in cmudict
            return None
    else:
        return None  # return None if word is not a string


def count_syllable(data: DataFrame) -> None:
    data['syllable_count']: DataFrame = data['Word'].apply(count_syllables)
    grouped: DataFrameGroupBy = data.groupby('syllable_count')

    LoadToSqlite().insert_to_sqlite(data, 'SyllableGroup')

    for name, group in grouped:
        output_path = f'dataset/{name}.tsv'
        save_data(group, output_path)


def get_stress_pattern(word: str) -> str | None:
    try:
        phonemes: str = pron_dict[word.lower()][0]  # Assumes word is in dictionary and takes first pronunciation
        stress_pattern = [char for phoneme in phonemes for char in phoneme if char.isdigit()]
        return ''.join(stress_pattern)
    except KeyError:  # Handles the case where the word is not in the dictionary
        return None


def get_stress_patterns(data: DataFrame) -> None:
    data['stress_pattern'] = data['Word'].apply(get_stress_pattern)


def get_primary_stress_position(stress_pattern: str) -> int:
    for i, char in enumerate(stress_pattern):
        if char == '1':
            return i + 1


def get_secondary_stress_position(stress_pattern: str) -> int:
    for i, char in enumerate(stress_pattern):
        if char == '2':
            return i + 1


def main() -> None:
    data_path = 'SUBTLEXus74286wordstextversion.tsv'
    dataset = load_data(data_path)
    count_syllable(dataset)

    engine = LoadToSqlite().sqlalchemy_engine
    query = "select * from main.SyllableGroup"
    df = pd.read_sql_query(query, engine)

    logger.info('Drop rows where \'syllable_count\' is null')
    df = df.dropna(subset=['syllable_count'])

    logger.info('Reset index after dropping rows')
    df.reset_index(drop=True, inplace=True)

    get_stress_patterns(df)

    df['primary_stress_position'] = df['stress_pattern'].apply(get_primary_stress_position)
    df['secondary_stress_position'] = df['stress_pattern'].apply(get_secondary_stress_position)

    LoadToSqlite().insert_to_sqlite(df, 'StressPattern')


if __name__ == '__main__':
    main()
