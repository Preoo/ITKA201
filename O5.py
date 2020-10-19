
def reverse_string(str_to_reverse:str) -> str:
    """
    Reverse swords in string

    >>> reverse_string('algoritmien opiskelu on kivaa')
    'kivaa on opiskelu algoritmien'

    Handle whitespace in string
    >>> reverse_string(' asd   123 ')
    '123 asd'
    """

    from string import whitespace

    words = []
    begin_marker = 0
    end_marker = len(str_to_reverse) - 1
    word_head = end_marker
    word_tail = end_marker

    while word_tail > begin_marker:
        while str_to_reverse[word_tail] in whitespace:
            word_tail = word_tail - 1

        word_head = word_tail - 1
        while word_head >= begin_marker and str_to_reverse[word_head] not in whitespace:
            word_head = word_head - 1

        words.append(str_to_reverse[word_head+1:word_tail+1])
        word_tail = word_head
    return ' '.join(words)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)