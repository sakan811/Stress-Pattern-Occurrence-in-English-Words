import pandas as pd
import pytest

from stress_pattern_etl import TransformWordData


def test_applies_count_syllables_to_word_column():
    # Given
    data = pd.DataFrame({'Word': ['apple', 'banana', 'orange']})
    transformer = TransformWordData()

    # When
    transformer.apply_count_syllable(data)

    # Then
    # Check that the syllable count is correct for each word
    assert data.loc[data['Word'] == 'apple', 'syllable_count'].values[0] == 2
    assert data.loc[data['Word'] == 'banana', 'syllable_count'].values[0] == 3
    assert data.loc[data['Word'] == 'orange', 'syllable_count'].values[0] == 2


def test_apply_count_syllable_handles_words_with_numbers():
    # Given
    data = pd.DataFrame({'Word': ['apple', 'banana', 'orange1']})
    transformer = TransformWordData()

    # When
    transformer.apply_count_syllable(data)

    # Then
    # Check that the syllable count is correct for each word
    assert data.loc[data['Word'] == 'apple', 'syllable_count'].values[0] == 2
    assert data.loc[data['Word'] == 'banana', 'syllable_count'].values[0] == 3
    assert data.loc[data['Word'] == 'orange1', 'syllable_count'].values[0] == -1


def test_empty_string_stress_pattern():
    # Given
    word = ""
    expected_stress_pattern = None

    # When
    result = TransformWordData._get_stress_pattern(word)

    # Then
    assert result == expected_stress_pattern


def test_empty_primary_stress_pattern():
    # Given
    stress_pattern = ""

    # When
    result = TransformWordData._get_primary_stress_position(stress_pattern)

    # Then
    assert result is None


def test_single_secondary_stress_position():
    # Given
    stress_pattern = "0102"

    # When
    result = TransformWordData._get_secondary_stress_position(stress_pattern)

    # Then
    assert result == 4


def test_empty_secondary_stress_pattern():
    # Given
    stress_pattern = ""

    # When
    result = TransformWordData._get_secondary_stress_position(stress_pattern)

    # Then
    assert result is None


if __name__ == '__main__':
    pytest.main()
