import nltk
from loguru import logger
from nltk.corpus import cmudict

from .extract_and_transform_syllable_data import TransformWordData
from .load_to_sqlite import LoadToSqlite

logger.info('Download the cmudict data.')
nltk.download('cmudict')
pron_dict = cmudict.dict()