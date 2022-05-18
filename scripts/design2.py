def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function return 2
    """

    words = text.split()
    return words.count(word)
    
    
def test_count_word_occurrence_in_string():
    assert count_word_occurrence_in_string("AAA BBB", "AAA") == 1
    assert count_word_occurrence_in_string("AAA AAA", "AAA") == 2
    assert count_word_occurrence_in_string("AAAAA", "AAA") == 0
