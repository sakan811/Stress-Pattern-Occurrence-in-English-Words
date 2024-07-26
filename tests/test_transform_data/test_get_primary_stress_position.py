from stress_pattern_finder.stress_pattern_etl.transform_data import get_primary_stress_position


def test_single_primary_stress():
    # Test with a stress pattern containing a single primary stress
    stress_pattern = "010"
    assert get_primary_stress_position(stress_pattern) == "2"


def test_multiple_primary_stresses():
    # Test with a stress pattern containing multiple primary stresses
    stress_pattern = "10101"
    assert get_primary_stress_position(stress_pattern) == "1,3,5"


def test_no_primary_stress():
    # Test with a stress pattern containing no primary stress
    stress_pattern = "000"
    assert get_primary_stress_position(stress_pattern) == ''


def test_empty_stress_pattern():
    # Test with an empty stress pattern
    stress_pattern = ""
    assert get_primary_stress_position(stress_pattern) == ''


def test_non_string_input():
    # Test with a non-string input
    stress_pattern = 123
    assert get_primary_stress_position(stress_pattern) is None


def test_invalid_stress_pattern():
    # Test with an invalid stress pattern
    stress_pattern = "abc"
    assert get_primary_stress_position(stress_pattern) == ''
