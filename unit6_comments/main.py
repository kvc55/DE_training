from logging_setup import logger


def count_chars(words: list) -> tuple:
    """Takes a list of words and counts their characters.

    :param words: words to process
    :type words: list
    :return: a list and a dictionary of counted characters
    :rtype: tuple
    """

    words = set(words)  # eliminates duplicates

    chars_count_list = [len(word) for word in words]
    chars_count_dict = {word: len(word) for word in words}

    return chars_count_list, chars_count_dict


if __name__ == '__main__':
    # list to process
    chars_count_list, chars_count_dict = count_chars(
        ['dog', 'elephant', 'dragon', 'dog'])

    logger.info(f'List of counted chars: {chars_count_list}')
    logger.info(f'Dictionary of counted chars: {chars_count_dict}')
