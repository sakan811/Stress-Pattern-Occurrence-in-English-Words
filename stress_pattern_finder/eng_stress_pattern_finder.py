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
from loguru import logger

from stress_pattern_etl import TransformWordData, LoadToSqlite


def find_stress_pattern(data_path: str) -> None:
    """
    Find stress patterns in English words within the given dataset.

    :param data_path: Dataset path
    :return: None
    """
    logger.info('Starting ETL process...')
    logger.info(f'Extract syllable data from {data_path}')
    dataset = pd.read_csv(data_path, delimiter='\t')
    TransformWordData().apply_count_syllable(dataset)

    dataset = TransformWordData().transform_word_data()

    LoadToSqlite().insert_to_sqlite(dataset, 'StressPattern')


if __name__ == '__main__':
    pass
