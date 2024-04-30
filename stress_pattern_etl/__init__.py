import nltk
from loguru import logger
from nltk.corpus import cmudict

logger.info('Download the cmudict data.')
nltk.download('cmudict')
pron_dict = cmudict.dict()