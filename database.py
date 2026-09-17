import logging

import mysql.connector

from config import DB_CONFIG


logger = logging.getLogger(__name__)


def create_connection():
    """Connect to the MySQL database."""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        logger.info("Connected to MySQL database.")

        return connection

    except mysql.connector.Error as error:
        logger.error("Database connection failed: %s", error)
        raise