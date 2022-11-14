from log_setup import logger


def convert_to_lowercase(fruits: list) -> None:
    """Converts list of fruits to lowercase

    :param fruits: List of fruits
    :type fruits: list
    """

    for fruit in fruits:
        try:
            logger.info(f'Conversion was ok: {fruit} ----> {fruit.lower()}')
        except Exception:
            logger.error(f'Could not convert: {fruit}')


if __name__ == "__main__":
    # list to process
    fruits = [
        'Blueberry',
        'Apple',
        'ORANGE',
        99.6,
        'BanaNa',
        'pEaR',
        'PeACh',
        99]

    convert_to_lowercase(fruits)
