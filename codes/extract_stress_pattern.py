import pandas as pd
import nltk
from nltk.corpus import cmudict

# Downloading the cmudict data outside the function, so it's only done once
nltk.download('cmudict')
pron_dict = cmudict.dict()


def load_data(data_path):
    # Added a return statement to return the loaded data
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
        group.to_csv(f'{name}_syllables.tsv', sep='\t', index=False)


def get_stress_pattern(word):
    # Removed the download statement and moved it outside the function
    try:
        phonemes = pron_dict[word.lower()][0]  # Assumes word is in dictionary and takes first pronunciation
        stress_pattern = [char for phoneme in phonemes for char in phoneme if char.isdigit()]
        return ''.join(stress_pattern)
    except KeyError:  # Handles the case where the word is not in the dictionary
        return None


def get_stress_patterns(data):
    data['stress_pattern'] = data['Word'].apply(get_stress_pattern)


def main():
    data_path = '6.0_syllables.tsv'
    dataframe = load_data(data_path)  # Store the returned data in a variable
    get_stress_patterns(dataframe)  # Call the new function to get stress patterns
    dataframe.to_csv('6_with_stress_patterns.tsv', sep='\t', index=False)  # Save the data with the new column to a file


if __name__ == '__main__':
    main()