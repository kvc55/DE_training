import pandas as pd

from logsetup import log_setup

logger = log_setup.logging.getLogger(__name__)


def process_data(file_path: str) -> pd.DataFrame:
    """Accepts a .xlsx file and processes it.

    :param file_path: Path to the file to be processed
    :type file_path: str
    :return: Information processed
    :rtype: pd.DataFrame
    """

    try:
        logger.info('Initializing data processing...')

        medals_df = pd.read_excel(file_path)
    except FileNotFoundError:
        logger.error('File not found')
    except Exception as e:
        logger.error('Error, something went wrong', e)
    else:
        # Filters information considering columns: Year, NOC and Medal
        medals_filtered_df = medals_df[(medals_df['Year'] >= 1950) &
                                       (medals_df['NOC'] == 'USA') &
                                       (medals_df['Medal'] == 'Gold')]
        logger.info('Data processing finished')

    return medals_filtered_df
