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
import os

import pandas as pd
from loguru import logger


def save_to_csv(dataframe: pd.DataFrame, directory: str) -> None:
    """
    Save the data into a csv file at the specified directory.
    :param dataframe: Dataframe to save.
    :param directory: Specified directory to save a CSV file.
    :return: None.
    """
    logger.info(f'Saving data to \'{directory}\' folder as CSV...')

    os.makedirs(directory, exist_ok=True)

    dataframe.to_csv(os.path.join(directory, 'eng_stress_patterns_data.csv'), index=False)


if __name__ == '__main__':
    pass