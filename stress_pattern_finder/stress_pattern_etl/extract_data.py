import pandas as pd
from loguru import logger


def extract_word_data(data_path: str):
    """
    Extract word data from the dataset.
    :param data_path: Dataset path.
    :return: None
    """
    logger.info(f'Extracting word data from the dataset...')
    try:
        dataset = pd.read_csv(data_path, delimiter='\t')
    except FileNotFoundError as e:
        logger.error(e)
        logger.error('File not found.')
        raise e
    else:
        logger.info(f'Extracted word data successfully.')
        return dataset
