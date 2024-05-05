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

import pandas as pd
from pandas import DataFrame
from loguru import logger
from nltk.corpus import cmudict
import nltk

from .load_to_sqlite import LoadToSqlite

logger.info('Download the cmudict data.')
nltk.download('cmudict')
pron_dict = cmudict.dict()


class TransformWordData:
    def __init__(self):
        pass

    @staticmethod
    def count_syllables(word: str) -> int | None:
        """
        Count the number of syllables in a word.
        :param word: English word.
        :return: Integer if the word is string, else None
        """
        if isinstance(word, str):  # check if word is a string
            try:
                return [len(list(y for y in x if y[-1].isdigit())) for x in pron_dict[word.lower()]][0]
            except KeyError as e:  # Handles the case where the word is not in the dictionary
                logger.error(f'KeyError: {e}')
                logger.error(f'{word} is not in CMU dictionary')
        else:
            return None  # return None if word is not a string

    def apply_count_syllable(self, data: DataFrame) -> None:
        """
        Apply 'count_syllables' function to 'Word' column
        :param data:
        :return:
        """
        logger.info(f"Applying \'count_syllables\' to DataFrame...")
        data['syllable_count']: DataFrame = data['Word'].apply(self.count_syllables)
        LoadToSqlite().insert_to_sqlite(data, 'SyllableGroup')

    @staticmethod
    def get_stress_pattern(word: str) -> str | None:
        """
        Get the stress pattern of a word.
        :param word: English word.
        :return: Stress pattern of a word as String, else None.
        """
        try:
            phonemes: str = pron_dict[word.lower()][0]  # Assumes word is in dictionary and takes first pronunciation
            stress_pattern = [char for phoneme in phonemes for char in phoneme if char.isdigit()]
            return ''.join(stress_pattern)
        except KeyError as e:  # Handles the case where the word is not in the dictionary
            logger.error(f'KeyError: {e}')
            logger.error(f'{word} is not in CMU dictionary')
            return None

    def apply_stress_patterns(self, data: DataFrame) -> None:
        """
        Apply 'get_stress_pattern' function to 'Word' column
        :param data: pandas DataFrame
        :return: None
        """
        logger.info(f"Applying \'get_stress_pattern\' to DataFrame...")
        data['stress_pattern'] = data['Word'].apply(self.get_stress_pattern)

    @staticmethod
    def get_primary_stress_position(stress_pattern: str) -> int:
        """
        Get the primary stress position of a word.
        :param stress_pattern: Stress pattern of a word.
        :return: Position of the primary stress as Integer.
        """
        for i, char in enumerate(stress_pattern):
            if char == '1':
                return i + 1

    @staticmethod
    def get_secondary_stress_position(stress_pattern: str) -> int:
        """
        Get the secondary stress position of a word.
        :param stress_pattern: Stress pattern of a word.
        :return: Position of the secondary stress as Integer.
        """
        for i, char in enumerate(stress_pattern):
            if char == '2':
                return i + 1

    def transform_word_data(self) -> pd.DataFrame:
        """
        Transform the English word data to find a syllable count and stress pattern.
        :return: Pandas DataFrame
        """
        engine = LoadToSqlite().sqlalchemy_engine
        query = "select * from main.SyllableGroup"
        df = pd.read_sql_query(query, engine)

        logger.info('Drop rows where \'syllable_count\' is null')
        df = df.dropna(subset=['syllable_count'])

        logger.info('Reset index after dropping rows')
        df.reset_index(drop=True, inplace=True)

        self.apply_stress_patterns(df)

        logger.info('Get primary stress position of each word')
        df['primary_stress_position'] = df['stress_pattern'].apply(self.get_primary_stress_position)
        logger.info('Get secondary stress position of each word')
        df['secondary_stress_position'] = df['stress_pattern'].apply(self.get_secondary_stress_position)

        return df


if __name__ == '__main__':
    pass
