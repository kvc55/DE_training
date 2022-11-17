import sqlalchemy as db
import pandas as pd

from logsetup import log_setup

logger = log_setup.logging.getLogger(__name__)
logger_result = log_setup.logging.getLogger('result')


class Database:
    """Creates the connection to the database.
       Creates, inserts, selects and updates information from medals table.
    """

    def __init__(self) -> None:
        """Creates the connection to the database.
        """

        # Connection to the database
        self.engine = db.create_engine('sqlite:///database/olympics.db')
        self.connection = self.engine.connect()

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
        self.connection.execute(query)
        logger.info('Table created successfully')

    def save_data(self, medals_filtered_df: pd.DataFrame) -> None:
        """Saves the new information in the table.

        :param medals_filtered_df: It has information about olympics
        :type customer: pd.Dataframe
        """

        medals_filtered_df.to_sql(
            name='medals',
            con=self.connection,
            if_exists='append',
            index=False)

    def fetch_info(self) -> None:
        """Retrieves information from the table.
        """

        query = "SELECT * FROM medals"
        data = pd.read_sql(query, con=self.connection)
        logger_result.info(data)
        self.connection.close()
