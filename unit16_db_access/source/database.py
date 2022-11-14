from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.exc import OperationalError

from log_config import logger
from settings import DB_URL
from models import Customer


class Database:
    """Creates the connection to the database.
       Inserts, selects, updates and deletes information from table customer.
    """

    def __init__(self) -> None:
        try:
            # Connection to the database
            self.engine = create_engine(DB_URL)
            self.connection = self.engine.connect()
            self.session = Session(bind=self.connection)
        except OperationalError:
            logger.error('Error when trying to connect to DB')
        except Exception as e:
            logger.error('An error has occurred', e)

    def create_customer(self, customer: Customer) -> None:
        """Saves the information of the new customer in a table.

        :param customer: It has all the information about the customer
        :type customer: Customer
        """

        try:
            self.session.add(customer)
            self.session.commit()
        except AttributeError:
            logger.error(
                'Could not save new customer due to an error connection')
        except Exception as e:
            logger.error(
                'An error has occurred when tyring to save new customer', e)

    def fetch_users_name(self) -> None:
        """Selects from table the customers' names and shows them.
        """

        try:
            meta = MetaData()
            customer = Table('customer', meta, Column('name'))
            data = self.connection.execute(customer.select())
        except AttributeError:
            logger.error(
                'Could not retrieve name due to an error connection')
        except Exception as e:
            logger.error(
                'An error has occurred when tyring to retrieve name', e)
        else:
            for user_name in data:
                logger.info(user_name)

    def fetch_users_info(self) -> None:
        """Selects from table the customers' information and shows it.
        """

        try:
            customers = self.session.query(Customer).all()
            self.session.commit()
        except AttributeError:
            logger.error(
                'Could not retrieve customers info due to an error connection')
        except Exception as e:
            logger.error(
                'An error has occurred when tyring to retrieve info', e)
        else:
            for customer in customers:
                logger.info(customer)

    def update_customer(self, customer_name: str, address: str) -> None:
        """Updates customer's address with the customer's name given.

        :param customer_name: The name of the user
        :type customer_name: str
        :param address: The address of the user
        :type address: str
        """

        try:
            data_to_update = {Customer.address: address}
            customer_name_filter = self.session.query(
                Customer).filter(Customer.name == customer_name)
            customer_name_filter.update(data_to_update)
            self.session.commit()
        except AttributeError:
            logger.error(
                'Could not update info due to an error connection')
        except Exception as e:
            logger.error(
                'An error has occurred when tyring to update info', e)

    def delete_customer(self, customer_name: str) -> None:
        """Deletes the customer from table with the given name.

        :param customer_name: Name of the user
        :type customer_name: str
        """

        try:
            customer_name_filter = self.session.query(Customer).filter(
                Customer.name == customer_name).first()
            self.session.delete(customer_name_filter)
            self.session.commit()
        except AttributeError:
            logger.error(
                'Could not delete customer due to an error connection')
        except Exception as e:
            logger.error(
                'An error has occurred when tyring to delete customer', e)


if __name__ == '__main__':
    data = Database()

    # Tries the different methods
    customer = Customer(
        'Jose',
        28,
        'jose@gmail.com',
        'Av. Rivadavia 1000',
        '8679')
        
    data.create_customer(customer)
    data.fetch_users_name()
    data.fetch_users_info()
    data.update_customer('Jose', 'Deheza 191')
    data.delete_customer('Jose')
