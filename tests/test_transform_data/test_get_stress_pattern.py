from stress_pattern_finder.stress_pattern_etl.transform_data import get_stress_pattern


def test_valid_word():
    # Test with a valid word
    word = "hello"
    assert get_stress_pattern(word) == "01"


def test_word_not_in_dictionary():
    # Test with a word not in the CMU dictionary
    word = "xylophone"
    assert get_stress_pattern(word) == "102"


def test_none_word():
    # Test with the word 'None'
    word = "None"
    assert get_stress_pattern(word) == '1'


def test_empty_string():
    # Test with an empty string
    word = ""
    assert get_stress_pattern(word) is None


def test_non_string_input():
    # Test with a non-string input
    word = 123
    assert get_stress_pattern(word) is None


def test_multiple_pronunciations():
    # Test with a word having multiple pronunciations
    word = "lead"
    assert get_stress_pattern(word) == "1"


def test_special_characters():
    # Test with a word containing special characters
    word = "café"
    assert get_stress_pattern(word) is None
