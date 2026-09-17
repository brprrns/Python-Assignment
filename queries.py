from database import create_connection


def get_employee_count():
    """Return the total number of employees."""
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees")

    result = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return result


def get_first_employees(limit=10):
    """Return the first few employees."""
    connection = create_connection()
    cursor = connection.cursor()

    query = """
        SELECT emp_no, first_name, last_name
        FROM employees
        LIMIT %s
    """

    cursor.execute(query, (limit,))

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees