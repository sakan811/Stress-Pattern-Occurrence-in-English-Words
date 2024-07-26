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

from loguru import logger
from pandas import DataFrame

from stress_pattern_finder.stress_pattern_etl.extract_data import extract_word_data
from stress_pattern_finder.stress_pattern_etl.transform_data import transform_word_data


def find_stress_pattern(data_path: str) -> DataFrame:
    """
    Find stress patterns in English words within the given dataset.

    :param data_path: Dataset path
    :return: Pandas Dataframe.
    """
    logger.info(f'Finding stress patterns in the dataset: {data_path}...')

    dataset = extract_word_data(data_path)

    return transform_word_data(dataset)


if __name__ == '__main__':
    pass
