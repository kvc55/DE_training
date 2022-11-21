import sqlalchemy as db
import pandas as pd
from sqlalchemy.exc import ArgumentError

from logsetup import log_setup

logger = log_setup.logging.getLogger(__name__)
logger_result = log_setup.logging.getLogger('result')

URL = 'sqlite:///database/olympics.db'


class Database:
    """Creates the connection to the database.
       Creates, inserts, selects and updates information from medals table.
    """

    def __init__(self) -> None:
        """Creates the connection to the database.
        """

        try:
            # Connection to the database
            self.engine = db.create_engine(URL)
            self.connection = self.engine.connect()
            logger.info('Connection to db was ok')
        except ArgumentError:
            logger.error('Could not connect to database')
        except Exception as e:
            logger.error('Something went wrong', e)

    def create_table(self) -> None:
        """Creates an empty table.
        """

        query = """CREATE TABLE IF NOT EXISTS medals (
                                                    Year INTEGER,
                                                    City TEXT,
                                                    Sport TEXT,
                                                    Discipline TEXT,
                                                    NOC TEXT,
                                                    Event TEXT,
                                                    'Event gender' TEXT,
                                                    Medal TEXT)"""
        try:
            self.connection.execute(query)
            logger.info('Table created successfully')
        except AttributeError:
            logger.error('Could not create table')
        except Exception as e:
            logger.error('Something went wrong', e)

    def save_data(self, medals_filtered_df: pd.DataFrame) -> None:
        """Saves the new information in the table.

        :param medals_filtered_df: It has information about olympics
        :type customer: pd.Dataframe
        """

        try:
            medals_filtered_df.to_sql(
                name='medals',
                con=self.connection,
                if_exists='append',
                index=False)

            logger.info('Data saved successfully')
        except AttributeError:
            logger.error('Could not save data')
        except Exception as e:
            logger.error('Something went wrong', e)

    def fetch_info(self) -> None:
        """Retrieves information from the table.
        """

        query = "SELECT * FROM medals"

        try:
            data_df = pd.read_sql(query, con=self.connection)
        except AttributeError:
            logger.error('Could not retrieve information')
        except Exception as e:
            logger.error('Something went wrong', e)
        else:
            logger_result.info(data_df)
            logger.info('Information retrieved successfully')
            self.connection.close()
