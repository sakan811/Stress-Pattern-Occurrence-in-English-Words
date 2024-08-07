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

import pandas as pd
from pandas import DataFrame
from loguru import logger
from nltk.corpus import cmudict
import nltk

from stress_pattern_finder.stress_pattern_etl.load_to_sqlite import insert_to_sqlite

logger.info('Download the cmudict data.')
nltk.download('cmudict')
pron_dict = cmudict.dict()


def count_syllables(word: str) -> int | None:
    """
    Count the number of syllables in a word.
    :param word: English word.
    :return: Integer if the word is string, else None
    """
    logger.debug(f"Counting syllables in '{word}'...")
    try:
        # Prevent the word 'None' to be considered as NoneType
        if word == 'None':
            word = 'none'

        syllable_count = [len(list(y for y in x if y[-1].isdigit())) for x in pron_dict[word.lower()]][0]
    except KeyError as e:  # Handles the case where the word is not in the dictionary
        logger.error(f'KeyError: {e}')
        logger.error(f'{word} is not in CMU dictionary')
        return None
    except TypeError as e:
        logger.error(f'TypeError: {e}')
        logger.error(f'{word} is not countable')
        return None
    except AttributeError as e:
        logger.error(e)
        logger.error(f'{word} is not String')
        return None
    else:
        logger.debug(f'Counted syllable in {word} successfully: {syllable_count = }')
        return syllable_count


def apply_count_syllable(data: DataFrame) -> DataFrame:
    """
    Count the number of syllables in a word.
    Take the word in each 'Word' column within the Dataframe and count the number of syllables.
    :param data: Pandas DataFrame.
    :return: Pandas DataFrame.
    """
    logger.info(f"Counting syllable of each word in the DataFrame...")

    data['syllable_count']: DataFrame = data['Word'].apply(count_syllables)

    logger.info('Drop rows where \'syllable_count\' is null')
    return data.dropna(subset=['syllable_count'])


def get_stress_pattern(word: str) -> str | None:
    """
    Get the stress pattern of a word.
    :param word: English word.
    :return: Stress pattern of a word as String, else None.
    """
    logger.debug(f'Getting stress pattern from {word}...')
    try:
        # Prevent the word 'None' to be considered as NoneType
        if word == 'None':
            word = 'none'

        phonemes: str = pron_dict[word.lower()][0]  # Assumes word is in dictionary and takes first pronunciation
        stress_pattern = [char for phoneme in phonemes for char in phoneme if char.isdigit()]
        return ''.join(stress_pattern)
    except KeyError as e:  # Handles the case where the word is not in the dictionary
        logger.error(f'KeyError: {e}')
        logger.error(f'{word} is not in CMU dictionary')
        return None
    except AttributeError as e:
        logger.error(e)
        logger.error(f'{word} is not String')
        return None


def get_primary_stress_position(stress_pattern: str) -> str | None:
    """
    Get the primary stress position of a word.
    :param stress_pattern: Stress pattern of a word.
    :return: Position of the primary stress as String, else None.
    """
    try:
        primary_stress_pos_list = []
        for i, char in enumerate(stress_pattern):
            if char == '1':
                primary_stress_pos_list.append(i + 1)
        return ','.join(str(primary_stress_pos) for primary_stress_pos in primary_stress_pos_list)
    except ValueError as e:
        logger.error(e)
        logger.error(f'{stress_pattern} value is not acceptable')
        return None
    except TypeError as e:
        logger.error(e)
        logger.error(f'{stress_pattern} is not String')
        return None


def get_secondary_stress_position(stress_pattern: str) -> str | None:
    """
    Get the secondary stress position of a word.
    :param stress_pattern: Stress pattern of a word.
    :return: Position of the secondary stress as String, else None.
    """
    try:
        secondary_stress_pos_list = []
        for i, char in enumerate(stress_pattern):
            if char == '2':
                secondary_stress_pos_list.append(i + 1)
        return ','.join(str(secondary_stress_pos) for secondary_stress_pos in secondary_stress_pos_list)
    except ValueError as e:
        logger.error(e)
        logger.error(f'{stress_pattern} value is not acceptable')
        return None
    except TypeError as e:
        logger.error(e)
        logger.error(f'{stress_pattern} is not String')
        return None


def transform_word_data(dataset: DataFrame) -> pd.DataFrame:
    """
    Transform the English word data to find a syllable count and stress pattern.
    :param dataset: Panda DataFrame.
    :return: Panda DataFrame.
    """
    data = apply_count_syllable(dataset)

    df = data.copy()

    df.loc[:, 'stress_pattern'] = df['Word'].apply(get_stress_pattern)

    logger.info('Get primary stress position of each word')
    df.loc[:, 'primary_stress_position'] = df['stress_pattern'].apply(get_primary_stress_position)
    logger.info('Get secondary stress position of each word')
    df.loc[:, 'secondary_stress_position'] = df['stress_pattern'].apply(get_secondary_stress_position)

    return df


if __name__ == '__main__':
    pass
