from datetime import datetime, timedelta

from log_setup import logger


class Employee():
    """Contains the characteristics of an employee.

    :param first_name: name of the employee
    :type first_name: str
    :param last_name: surname of the employee
    :type last_name: str
    :param birth_date: birth date of the employee
    :type birth_date: str
    :param dni_number: DNI of the employee
    :type dni_number: str
    """

    def __init__(self, first_name: str, last_name: str,
                 birth_date: str, dni_number: str) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        self.dni_number = dni_number

    def get_age(self) -> str:
        """Obtains employee's age using birth date.

        :return: Age of the employee
        :rtype: str
        """

        return (
            f"I'm "
            f"{(datetime.today() - self.birth_date) // timedelta(days=365.24)}"
            f" years old.")

    def introduce_person(self) -> str:
        """Obtains employee's information.

        :return: Information of the employee
        :rtype: str
        """

        birth = self.birth_date.strftime("%d-%m-%Y")
        return (
            f"I'm {self.first_name} {self.last_name}. I was born"
            f"on {birth} and my dni number is {self.dni_number}.")


if __name__ == '__main__':
    # Tries the different methods
    employee_1 = Employee('María', 'Pérez', '1993-08-12', '37621590')
    logger.info(employee_1.get_age())
    logger.info(employee_1.introduce_person())
