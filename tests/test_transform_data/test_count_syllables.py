from stress_pattern_finder.stress_pattern_etl.transform_data import TransformWordData


def test_count_syllables_common_word():
    # Given
    transformer = TransformWordData()
    word = "example"
    expected_syllable_count = 3

    # When
    syllable_count = transformer._count_syllables(word)

    # Then
    assert syllable_count == expected_syllable_count


def test_handle_word_not_in_dictionary():
    # Given
    transformer = TransformWordData()
    word = "qwertyuiop"  # Assuming this word is not in the CMU dictionary

    # When
    syllable_count = transformer._count_syllables(word)

    # Then
    assert syllable_count is None


def test_handle_string_none_input():
    # Given
    word = 'None'

    # When
    result = TransformWordData._count_syllables(word)

    # Then
    assert result is not None


def test_handle_empty_string_input():
    # Given
    word = ""

    # When
    result = TransformWordData._count_syllables(word)

    # Then
    assert result is None
