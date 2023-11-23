import pandas as pd
import nltk
from nltk.corpus import cmudict

# Downloading the cmudict data outside the function, so it's only done once
nltk.download('cmudict')
pron_dict = cmudict.dict()


def load_data(data_path):
    return pd.read_csv(data_path, delimiter='\t')


def save_data(data, output_path):
    data.to_csv(output_path, sep='\t', index=False)


def count_syllables(word):
    if isinstance(word, str):  # check if word is a string
        try:
            return [len(list(y for y in x if y[-1].isdigit())) for x in pron_dict[word.lower()]][0]
        except KeyError:
            # handle case where word is not in cmudict
            return None
    else:
        return None  # return None if word is not a string


def count_syllable(data):
    data['syllable_count'] = data['Word'].apply(count_syllables)
    grouped = data.groupby('syllable_count')

    for name, group in grouped:
        output_path = f'../dataset/Syllables/{name}_syllables.tsv'
        save_data(group, output_path)


def get_stress_pattern(word):
    try:
        phonemes = pron_dict[word.lower()][0]  # Assumes word is in dictionary and takes first pronunciation
        stress_pattern = [char for phoneme in phonemes for char in phoneme if char.isdigit()]
        return ''.join(stress_pattern)
    except KeyError:  # Handles the case where the word is not in the dictionary
        return None


def get_stress_patterns(data):
    data['stress_pattern'] = data['Word'].apply(get_stress_pattern)


def main():
    dataset = load_data('../dataset/SUBTLEXus74286wordstextversion.tsv')
    count_syllable(dataset)

    for i in range(2, 7):
        data_path = f'../dataset/Syllables/{i}.0_syllables.tsv'
        dataframe = load_data(data_path)
        get_stress_patterns(dataframe)
        output_path = (f'../dataset/Syllables with Stress '
                       f'Pattern/{i}_with_stress_patterns.tsv')
        save_data(dataframe, output_path)


if __name__ == '__main__':
    main()