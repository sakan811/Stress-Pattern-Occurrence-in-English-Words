import pandas as pd

from stress_pattern_finder.stress_pattern_etl.transform_data import apply_count_syllable


def test_apply_count_syllable():
    # Sample data
    data = pd.DataFrame({
        'Word': ['hello', 'world', 'python', 'is', 'great', None, '', '123', 'syllable']
    })

    # Apply the syllable counting method
    loader = apply_count_syllable(data)

    # Check if the syllable counts are correctly calculated
    assert loader['syllable_count'].tolist() == [2.0, 1.0, 2.0, 1.0, 1.0, 3.0]

    # Check if rows with null syllable counts are dropped
    assert loader.shape[0] == 6


def test_empty_dataframe():
    # Empty DataFrame
    data = pd.DataFrame(columns=['Word'])

    # Apply the syllable counting method
    result = apply_count_syllable(data)

    # Check if the result is still an empty DataFrame
    assert result.empty


def test_dataframe_with_null_values():
    # DataFrame with null values
    data = pd.DataFrame({
        'Word': ['hello', None, 'world', None, 'python']
    })

    # Apply the syllable counting method
    result = apply_count_syllable(data)

    # Expected syllable counts
    expected_syllable_counts = [2.0, 1.0, 2.0]

    # Check if the syllable counts are correctly calculated
    assert result['syllable_count'].tolist() == expected_syllable_counts

    # Check if rows with null values are dropped
    assert result.shape[0] == 3


def test_dataframe_with_empty_strings():
    # DataFrame with empty strings
    data = pd.DataFrame({
        'Word': ['hello', '', 'world', '', 'python']
    })

    # Apply the syllable counting method
    result = apply_count_syllable(data)

    # Expected syllable counts
    expected_syllable_counts = [2.0, 1.0, 2.0]

    # Check if the syllable counts are correctly calculated
    assert result['syllable_count'].tolist() == expected_syllable_counts

    # Check if rows with empty strings are dropped
    assert result.shape[0] == 3


def test_dataframe_with_non_string_values():
    # DataFrame with non-string values
    data = pd.DataFrame({
        'Word': ['hello', 123, 'world', 456.78, 'python']
    })

    # Apply the syllable counting method
    result = apply_count_syllable(data)

    # Expected syllable counts
    expected_syllable_counts = [2.0, 1.0, 2.0]

    # Check if the syllable counts are correctly calculated
    assert result['syllable_count'].tolist() == expected_syllable_counts

    # Check if rows with non-string values are dropped
    assert result.shape[0] == 3


def test_all_rows_dropped():
    # DataFrame with all rows having null or non-string values
    data = pd.DataFrame({
        'Word': [None, '', 123, None, 456.78]
    })

    # Apply the syllable counting method
    result = apply_count_syllable(data)

    # Check if all rows are dropped
    assert result.empty
