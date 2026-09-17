import logging

from database import create_connection


logger = logging.getLogger(__name__)


def employee_generator(batch_size=1000):
    """Generate employees in small batches."""
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT emp_no, first_name, last_name
        FROM employees
    """

    try:
        cursor.execute(query)

        while True:
            rows = cursor.fetchmany(batch_size)

            if not rows:
                break

            for row in rows:
                yield row

    except Exception as error:
        logger.error("Error while fetching employees: %s", error)
        raise

    finally:
        cursor.close()
        connection.close()

        logger.info("Database connection closed.")