import pytest

import stress_pattern_finder


def test_full_process():
    data_path = '../SUBTLEXus74286wordstextversion.tsv'
    stress_pattern_finder.find_stress_pattern(data_path)


if __name__ == '__main__':
    pytest.main([__file__])
