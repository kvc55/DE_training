from src.extraction import extract_data
from src.processing import process_data
from src.loading import Database
from logsetup import log_setup

logger = log_setup.logging.getLogger(__name__)

if __name__ == '__main__':

    logger.info('Initializing process... ')

    # Download the information
    file_path = extract_data()

    # Extracts part of the data
    medals_filtered_df = process_data(file_path)

    # Operations with database
    db_access = Database()
    db_access.create_table()
    db_access.save_data(medals_filtered_df)
    db_access.fetch_info()

    logger.info('Process finished')
