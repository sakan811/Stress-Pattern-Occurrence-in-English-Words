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
    def _apply_count_syllable(data: DataFrame) -> None:
        """
        Count the number of syllables in a word.
        Take the word in each 'Word' column within the Dataframe and count the number of syllables.
        :param data: Pandas DataFrame
        :return: None
        """
        logger.info(f"Counting syllable of each word in the DataFrame...")

        def count_syllables(word: str) -> int | None:
            """
            Count the number of syllables in a word.
            :param word: English word.
            :return: Integer if the word is string, else None
            """
            logger.info(f"Counting syllables in '{word}'...")
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
                logger.info(f'Counted syllable in {word} successfully: {syllable_count = }')
                return syllable_count

        data['syllable_count']: DataFrame = data['Word'].apply(count_syllables)

        logger.info('Drop rows where \'syllable_count\' is null')
        data = data.dropna(subset=['syllable_count'])

        LoadToSqlite().insert_to_sqlite(data, 'SyllableGroup')

    @staticmethod
    def _get_stress_pattern(word: str) -> str | None:
        """
        Get the stress pattern of a word.
        :param word: English word.
        :return: Stress pattern of a word as String, else None.
        """
        logger.info(f'Getting stress pattern from {word}...')
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

    @staticmethod
    def _get_primary_stress_position(stress_pattern: str) -> int | None:
        """
        Get the primary stress position of a word.
        :param stress_pattern: Stress pattern of a word.
        :return: Position of the primary stress as Integer, else None.
        """
        try:
            for i, char in enumerate(stress_pattern):
                if char == '1':
                    return i + 1
        except ValueError as e:
            logger.error(e)
            logger.error(f'{stress_pattern} value is not acceptable')
            return None
        except TypeError as e:
            logger.error(e)
            logger.error(f'{stress_pattern} is not String')
            return None

    @staticmethod
    def _get_secondary_stress_position(stress_pattern: str) -> int | None:
        """
        Get the secondary stress position of a word.
        :param stress_pattern: Stress pattern of a word.
        :return: Position of the secondary stress as Integer, else None.
        """
        try:
            for i, char in enumerate(stress_pattern):
                if char == '2':
                    return i + 1
        except ValueError as e:
            logger.error(e)
            logger.error(f'{stress_pattern} value is not acceptable')
            return None
        except TypeError as e:
            logger.error(e)
            logger.error(f'{stress_pattern} is not String')
            return None

    def transform_word_data(self, dataset: DataFrame) -> pd.DataFrame:
        """
        Transform the English word data to find a syllable count and stress pattern.
        :param dataset: Panda DataFrame.
        :return: Panda DataFrame.
        """
        self._apply_count_syllable(dataset)

        engine = LoadToSqlite().sqlalchemy_engine
        query = "select * from main.SyllableGroup"
        df = pd.read_sql_query(query, engine)

        logger.info('Reset index after dropping rows')
        df.reset_index(drop=True, inplace=True)

        df['stress_pattern'] = df['Word'].apply(self._get_stress_pattern)

        logger.info('Get primary stress position of each word')
        df['primary_stress_position'] = df['stress_pattern'].apply(self._get_primary_stress_position)
        logger.info('Get secondary stress position of each word')
        df['secondary_stress_position'] = df['stress_pattern'].apply(self._get_secondary_stress_position)

        return df


if __name__ == '__main__':
    pass
