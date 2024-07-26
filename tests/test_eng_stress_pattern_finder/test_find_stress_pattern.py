import pandas as pd
import pytest
from pandas import DataFrame

from stress_pattern_finder.eng_stress_pattern_finder import find_stress_pattern


def test_successful_extraction_of_word_data(mocker):
    # Given
    data_path = 'valid_dataset_path.tsv'
    mock_dataset = DataFrame({'Word': ['example'], 'SyllableCount': [3]})
    mocker.patch('stress_pattern_finder.eng_stress_pattern_finder.extract_word_data', return_value=mock_dataset)
    mocker.patch('stress_pattern_finder.eng_stress_pattern_finder.transform_word_data', return_value=mock_dataset)

    # When
    result = find_stress_pattern(data_path)

    # Then
    assert not result.empty
    assert 'Word' in result.columns
    assert 'SyllableCount' in result.columns


def test_handle_file_not_found_error(mocker):
    # Given
    data_path = 'invalid_dataset_path.tsv'
    mocker.patch('stress_pattern_finder.eng_stress_pattern_finder.extract_word_data', side_effect=FileNotFoundError)

    # When / Then
    with pytest.raises(FileNotFoundError):
        find_stress_pattern(data_path)


def test_transform_data_to_find_syllable_count_and_stress_patterns():
    # Given
    data_path = 'tests/SUBTLEXus74286wordstextversion.tsv'
    expected_columns = [
        "Word",
        "FREQcount",
        "CDcount",
        "FREQlow",
        "Cdlow",
        "SUBTLWF",
        "Lg10WF",
        "SUBTLCD",
        "Lg10CD",
        "syllable_count",
        "stress_pattern",
        "primary_stress_position",
        "secondary_stress_position"
    ]

    # When
    result = find_stress_pattern(data_path)

    # Then
    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == expected_columns
