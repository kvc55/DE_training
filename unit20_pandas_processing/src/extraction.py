import pandas as pd
from urllib.error import HTTPError

from logsetup import log_setup

logger = log_setup.logging.getLogger(__name__)

URL = 'http://winterolympicsmedals.com/medals.csv'


def extract_data() -> str:
    """Downloads .cvs file from URL given and saves it as .xlsx file.

    :return: Path to .xlsx file
    :rtype: str
    """

    file_path = 'downloads/medals.xlsx'

    try:
        logger.info('Initializing data extraction...')

        medals_df = pd.read_csv(URL)
        medals_df.to_excel(file_path, index=False)
    except HTTPError:
        logger.error('Error when trying to download file')
    except Exception as e:
        logger.error('Something went wrong', e)
    else:
        logger.info('Data extraction finished')

    return file_path
