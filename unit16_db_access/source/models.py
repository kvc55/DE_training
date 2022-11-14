from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Does the mapping from the metainformation
Base = declarative_base()


class Customer(Base):
    """It holds the customer table structure.

    :param name: The name of the user
    :type name: str
    :param age: The age of the user
    :type age: int
    :param email: The email of the user
    :type email: str
    :param address: The adress of the user
    :type address: str
    :param zip_code: The zip_code of the user
    :type zip_code: str
    """    """"""

    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)

    def __init__(
            self,
            name: str,
            age: int,
            email: str,
            address: str,
            zip_code: str) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code

    def __repr__(self) -> str:
        """It shows the customer information.

        :return: Customer information
        :rtype: str
        """        """"""
        return (f"""<Customer({self.name}, {self.age}, {self.email}, """
                f"""{self.address}, {self.zip_code})>""")
