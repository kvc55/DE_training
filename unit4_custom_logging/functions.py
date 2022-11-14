from log_setup import logger2


def count_rows(file_info: str, file_name: str) -> int:
    """Takes the text and counts number of rows and words per row.

    :param file_info: file information
    :type file_info: str
    :param file_name: name of the file
    :type file_name: str
    :return: rows count
    :rtype: int
    """

    rows_list = file_info.split('\n')

    logger2.info(f'{file_name} - Total rows: {len(rows_list)}')

    for row in rows_list:
        words = row.split(' ')

        logger2.info(f'Row {rows_list.index(row)}: {len(words)} words')

    return len(rows_list)
