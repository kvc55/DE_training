import requests
from pathlib import Path, WindowsPath

from logsetup import log_setup

logger = log_setup.logging.getLogger(__name__)


def extract_data() -> WindowsPath:
    """Downloads .cvs file from URL given.

    :return: Path to .csv file
    :rtype: WindowsPath
    """

    url = 'http://winterolympicsmedals.com/medals.csv'

    logger.info('Initializing data extraction...')
    
    # Create path to save the .csv file
    b_path = Path(str(Path(__file__).resolve().parent.parent) + '/downloads')
    f_path = 'medals.csv'
    final_path = b_path / f_path

    # Create directory
    b_path.mkdir(parents=True, exist_ok=True)

    r = requests.get(url).content

    # Save .csv file
    with open(final_path, 'wb') as file:
        file.write(r)

    logger.info('Data extraction finished')

    return final_path
