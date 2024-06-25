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
import sys

from loguru import logger

from stress_pattern_finder.eng_stress_pattern_finder import find_stress_pattern
from stress_pattern_finder.stress_pattern_etl.load_to_sqlite import LoadToSqlite
from stress_pattern_finder.stress_pattern_etl.utils import save_to_csv

logger.configure(handlers=[{'sink': sys.stderr, 'level': 'INFO'}])
logger.add(
    'extract_stress_pattern.log',
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name} | {module} | {function} | {line} | {message}",
    mode='w', level='INFO'
)

if __name__ == '__main__':
    data_path = 'SUBTLEXus74286wordstextversion.tsv'
    dataframe = find_stress_pattern(data_path)
    save_to_csv(dataframe, directory='data')
    LoadToSqlite().insert_to_sqlite(dataframe, 'StressPattern')
