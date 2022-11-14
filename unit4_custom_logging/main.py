import functions
from log_setup import logger1


def process_text(file_name: str) -> int:
    """Takes the text file and opens it.

    :param file_name: text to be opened
    :type file_name: str
    :return: number of rows
    :rtype: int
    """

    try:
        with open(file_name, 'r') as f:
            logger1.info('...Reading file...')

            file_info = f.read()
            row_count = functions.count_rows(file_info, file_name)

            logger1.info('...File was processed...')

            return row_count
    except OSError:
        logger1.error('Could not open file')


if __name__ == '__main__':
    process_text('unit4_logging2/resources/story.txt')
