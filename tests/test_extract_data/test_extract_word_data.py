import pytest

from stress_pattern_finder.stress_pattern_etl.extract_data import extract_word_data


def test_successfully_reads_valid_tsv_file():
    data_path = 'tests/SUBTLEXus74286wordstextversion.tsv'
    df = extract_word_data(data_path)
    assert not df.empty
    assert df.shape == (74286, 9)


def test_file_not_found():
    # Given
    data_path = 'non_existent_file.tsv'

    # When / Then
    with pytest.raises(FileNotFoundError):
        extract_word_data(data_path)
