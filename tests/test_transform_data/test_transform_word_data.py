import pandas as pd

from stress_pattern_finder.stress_pattern_etl.transform_data import transform_word_data


def test_transform_valid_words():
    # Given
    data = pd.DataFrame({'Word': ['hello', 'world']})
    expected_syllable_counts = [2, 1]
    expected_stress_patterns = ['01', '1']
    expected_primary_stress_positions = ['2', '1']
    expected_secondary_stress_positions = ['', '']

    # When
    result = transform_word_data(data)

    # Then
    assert result['syllable_count'].tolist() == expected_syllable_counts
    assert result['stress_pattern'].tolist() == expected_stress_patterns
    assert result['primary_stress_position'].tolist() == expected_primary_stress_positions
    assert result['secondary_stress_position'].tolist() == expected_secondary_stress_positions


def test_handle_words_not_in_dictionary():
    # Given
    data = pd.DataFrame({'Word': ['nonexistentword']})
    expected_syllable_counts = []
    expected_stress_patterns = []
    expected_primary_stress_positions = []
    expected_secondary_stress_positions = []


    # When
    result = transform_word_data(data)

    # Then
    assert result.empty
    assert result['syllable_count'].tolist() == expected_syllable_counts
    assert result['stress_pattern'].tolist() == expected_stress_patterns
    assert result['primary_stress_position'].tolist() == expected_primary_stress_positions
    assert result['secondary_stress_position'].tolist() == expected_secondary_stress_positions