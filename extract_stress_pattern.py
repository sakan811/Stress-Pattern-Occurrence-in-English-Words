import os
import pandas as pd
import nltk
from nltk.corpus import cmudict
from pandas import DataFrame
from pandas.core.groupby import DataFrameGroupBy

# Downloading the cmudict data outside the function, so it's only done once
nltk.download('cmudict')
pron_dict = cmudict.dict()


def load_data(dataset_path: str) -> DataFrame:
    return pd.read_csv(dataset_path, delimiter='\t')


def save_data(data: DataFrame, output_path: str) -> None:
    data.to_csv(output_path, sep='\t', index=False)


def count_syllables(word: str):
    if isinstance(word, str):  # check if word is a string
        try:
            return [len(list(y for y in x if y[-1].isdigit())) for x in pron_dict[word.lower()]][0]
        except KeyError:
            # handle case where word is not in cmudict
            return None
    else:
        return None  # return None if word is not a string


def count_syllable(data: DataFrame) -> None:
    data['syllable_count']: DataFrame = data['Word'].apply(count_syllables)
    grouped: DataFrameGroupBy = data.groupby('syllable_count')

    for name, group in grouped:
        output_path = f'dataset/{name}.tsv'
        save_data(group, output_path)


def get_stress_pattern(word: str) -> str | None:
    try:
        phonemes: str = pron_dict[word.lower()][0]  # Assumes word is in dictionary and takes first pronunciation
        stress_pattern = [char for phoneme in phonemes for char in phoneme if char.isdigit()]
        return ''.join(stress_pattern)
    except KeyError:  # Handles the case where the word is not in the dictionary
        return None


def get_stress_patterns(data: DataFrame) -> None:
    data['stress_pattern'] = data['Word'].apply(get_stress_pattern)


def main() -> None:
    data_path = 'SUBTLEXus74286wordstextversion.tsv'
    dataset = load_data(data_path)
    count_syllable(dataset)
    syllable_count = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 12]

    for i in syllable_count:
        data_path = f'dataset/{i}.0.tsv'
        dataframe: DataFrame = load_data(data_path)
        get_stress_patterns(dataframe)
        output_path = f'dataset/with_stress_pattern/{i}_with_stress_patterns.tsv'
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        save_data(dataframe, output_path)


if __name__ == '__main__':
    main()