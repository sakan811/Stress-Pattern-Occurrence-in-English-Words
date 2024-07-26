from stress_pattern_finder.stress_pattern_etl.transform_data import count_syllables


def test_count_syllables_common_word():
    # Given
    word = "example"
    expected_syllable_count = 3

    # When
    syllable_count = count_syllables(word)

    # Then
    assert syllable_count == expected_syllable_count


def test_handle_word_not_in_dictionary():
    # Given
    word = "qwertyuiop"  # Assuming this word is not in the CMU dictionary

    # When
    syllable_count = count_syllables(word)

    # Then
    assert syllable_count is None


def test_handle_string_none_input():
    # Given
    word = 'None'

    # When
    result = count_syllables(word)

    # Then
    assert result is not None


def test_handle_empty_string_input():
    # Given
    word = ""

    # When
    result = count_syllables(word)

    # Then
    assert result is None
