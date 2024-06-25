import pytest

from stress_pattern_finder.eng_stress_pattern_finder import find_stress_pattern


def test_full_process():
    data_path = 'SUBTLEXus74286wordstextversion.tsv'
    df = find_stress_pattern(data_path)
    assert not df.empty

    # Check columns
    assert df.shape[1] == 13


if __name__ == '__main__':
    pytest.main([__file__])
