import os
from dotenv import load_dotenv
import logging
from scraper import crawl
import psycopg2

load_dotenv()
logger = logging.getLogger()
SOURCE = os.getenv("SOURCE")
STATS_PAGE = os.getenv("STATS_PAGE")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")


def main():
    logging.basicConfig(level=logging.INFO)

    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        logger.info("Successfully connected to PostgreSQL database!")

    except Exception as error:
        logger.info(f"Error connecting to database: {error}")

    crawl(SOURCE+STATS_PAGE)

if __name__ == '__main__':
    main()