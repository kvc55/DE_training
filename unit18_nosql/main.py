import pandas as pd
from pymongo import MongoClient
from pymongo import database
from pymongo.collection import Collection
from pymongo.errors import (
    ConnectionFailure,
    ServerSelectionTimeoutError,
    DuplicateKeyError,
    OperationFailure,
    BulkWriteError)

from logsetup import log_setup

logger = log_setup.logging.getLogger(__name__)
logger_r = log_setup.logging.getLogger('result')

URI = 'mongodb://localhost:27017/'


class Database:
    """Creates the connection and the database.
       Inserts, selects and updates information from database.
    """

    def __init__(self) -> None:
        try:
            self.client = MongoClient(URI, serverSelectionTimeoutMS=5000)
            self.client.server_info()
        except ConnectionFailure:
            logger.error('Unable to connect to the server')

    def create_database(self) -> database.Database:
        """Creates a database.

        :return: Database created
        :rtype: database.Database
        """

        return self.client['unit18']

    def create_collection(self, db_name: database.Database) -> Collection:
        """Creates two collections.

        :param db_name: Database created
        :type db_name: database.Database
        :return: The two collections created
        :rtype: collection.Collection
        """

        collection_books = db_name["Books"]
        collection_client = db_name["Client"]

        return collection_books, collection_client

    def insert_one_document(
            self,
            collection_books: Collection,
            collection_client: Collection) -> None:
        """Inserts one document in each collection.

        :param collection_books: Collection of information about books
        :type collection_books: Collection
        :param collection_client: Collection of information about clients
        :type collection_client: Collection
        """

        # Dicts to insert
        books_item_1 = {
            '_id': 1,
            'Name': 'Alice in Wonderland',
            'Author': 'Lewis Carrol',
            'Genre': 'Fantasy'}

        client_item_1 = {
            '_id': 1,
            'Name': 'Mary'}

        try:
            collection_books.insert_one(books_item_1)
            collection_client.insert_one(client_item_1)
        except ServerSelectionTimeoutError:
            logger.error('Error when trying to insert document')
        except DuplicateKeyError:
            logger.error('Index already exists')
        except OperationFailure as e:
            logger.error('Error when trying to insert document', e)

    def insert_many_documents(
            self,
            collection_books: Collection,
            collection_client: Collection) -> None:
        """Inserts many documents in each collection.

        :param collection_books: Collection of information about books
        :type collection_books: Collection
        :param collection_client: Collection of information about clients
        :type collection_client: Collection
        """

        # Dicts to insert
        books_items = [{'_id': 2,
                        'Name': 'Adventures of Tom Sawyer',
                        'Author': 'Mark Twain'},
                       {'_id': 3,
                        'Name': 'A passage to India',
                        'Author': 'E.M.Forster'}]

        client_items = [{'_id': 2,
                         'Name': 'Peter',
                         'LastName': 'Gomez'},
                        {'_id': 3,
                         'Name': 'Sara',
                         'City': 'Cordoba'}]

        try:
            collection_books.insert_many(books_items)
            collection_client.insert_many(client_items)
        except ServerSelectionTimeoutError:
            logger.error('Error when trying to insert documents')
        except BulkWriteError:
            logger.error('Error when trying to insert documents')
        except OperationFailure as e:
            logger.error('Error when trying to insert documents', e)

    def show_items_collection(
            self,
            collection_books: Collection,
            collection_client: Collection) -> None:
        """Shows all items in each collection.

        :param collection_books: Collection of information about books
        :type collection_books: Collection
        :param collection_client: Collection of information about clients
        :type collection_client: Collection
        """

        try:
            items_collection_books = collection_books.find()
            items_books_df = pd.DataFrame(items_collection_books)
            logger_r.info(items_books_df)

            items_collection_client = collection_client.find()
            items_client_df = pd.DataFrame(items_collection_client)
            logger_r.info(items_client_df)

        except ServerSelectionTimeoutError:
            logger.error('Error when trying to show items')

    def show_specific_item(
            self,
            collection_books: Collection,
            collection_client: Collection) -> None:
        """Shows a specific item in each collection.

        :param collection_books: Collection of information about books
        :type collection_books: Collection
        :param collection_client: Collection of information about clients
        :type collection_client: Collection
        """

        try:
            item_books = collection_books.find({'Author': 'Mark Twain'})
            item_books_df = pd.DataFrame(item_books)
            logger_r.info(item_books_df)

            item_client = collection_client.find({'City': 'Cordoba'})
            item_client_df = pd.DataFrame(item_client)
            logger_r.info(item_client_df)

        except ServerSelectionTimeoutError:
            logger.error('Error when trying to show an item')

    def update_one_document(
            self,
            collection_books: Collection,
            collection_client: Collection) -> None:
        """Updates one document in each collection.

        :param collection_books: Collection of information about books
        :type collection_books: Collection
        :param collection_client: Collection of information about clients
        :type collection_client: Collection
        """

        try:
            result_books = collection_books.update_one(
                {'_id': 1}, {'$set': {'InStock': 'No'}})
            result_client = collection_client.update_one(
                {'_id': 2}, {'$set': {'Name': 'Peter Adrei'}})

            # When it doesn't find results
            if result_books.matched_count == 0:
                raise OperationFailure(
                    'Could not update doc from Books collection')
            elif result_client.matched_count == 0:
                raise OperationFailure(
                    'Could not update doc from Client collection')

        except ServerSelectionTimeoutError:
            logger.error('Error when trying to update one document')

    def update_many_documents(
            self,
            collection_books: Collection,
            collection_client: Collection) -> None:
        """Updates many documents in each collection.

        :param collection_books: Collection of information about books
        :type collection_books: Collection
        :param collection_client: Collection of information about clients
        :type collection_client: Collection
        """

        try:
            result_books = collection_books.update_many(
                {'_id': {'$gt': 1}}, {'$set': {'Genre': 'Realistic'}})
            result_client = collection_client.update_many(
                {}, {'$set': {'Bill': 'Yes'}})

            # When it doesn't find results
            if result_books.matched_count == 0:
                raise OperationFailure(
                    'Could not update docs from Books collection')
            elif result_client.matched_count == 0:
                raise OperationFailure(
                    'Could not update docs from Client collection')

        except ServerSelectionTimeoutError:
            logger.error('Error when trying to update documents')


if __name__ == '__main__':
    # Object from class Database
    database = Database()

    # Basic operations to do in database
    db_name = database.create_database()

    collection_books, collection_client = database.create_collection(db_name)

    database.insert_one_document(collection_books, collection_client)

    database.insert_many_documents(collection_books, collection_client)

    database.show_items_collection(collection_books, collection_client)

    database.show_specific_item(collection_books, collection_client)

    database.update_one_document(collection_books, collection_client)

    database.update_many_documents(collection_books, collection_client)
