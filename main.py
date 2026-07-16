import os
from dotenv import load_dotenv
import logging
from scraper import crawl
load_dotenv()
logger = logging.getLogger()
SOURCE = os.getenv("SOURCE")
STATS_PAGE = os.getenv("STATS_PAGE")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")


def main():
    logging.basicConfig(level=logging.INFO)

    # truncates file every re-run
    with open('test.txt', 'w') as f:
        pass

    crawl(SOURCE+STATS_PAGE)

if __name__ == '__main__':
    main()