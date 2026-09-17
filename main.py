import logging

from generator import employee_generator
from logging_config import setup_logging
from queries import get_employee_count, get_first_employees


logger = logging.getLogger(__name__)


def main():
    setup_logging()

    try:
        count = get_employee_count()
        print("Total employees:", count)

        print("\nFirst 10 employees:")

        for employee in get_first_employees():
            print(employee)

        print("\nProcessing all employees...")

        processed = 0

        for employee in employee_generator():
            processed += 1

        print("Employees processed:", processed)

    except Exception as error:
        logger.error("Something went wrong: %s", error)


if __name__ == "__main__":
    main()