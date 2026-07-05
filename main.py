import os
from dotenv import load_dotenv
from pandas.core.interchange.dataframe_protocol import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
import logging

load_dotenv()
logger = logging.getLogger()
SOURCE = os.getenv("SOURCE")
STATS_PAGE = os.getenv("STATS_PAGE")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")


def crawl(path: str):
    driver = webdriver.Chrome()


    cookies_selector = 'button.fc-cta-consent.fc-primary-button'
    driver.get(path)
    driver.wait = WebDriverWait(driver, 5)

    cookies = driver.find_elements(By.CSS_SELECTOR, cookies_selector)
    if len(cookies) > 0:
        cookies[0].click()
        logger.info("Cookies clicked")
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, 'div[class*=TLStatsTopThreeCSS] > a')
        category_links = [el.get_attribute('href') for el in elements]
        category_names = driver.find_elements(By.CSS_SELECTOR, 'h3[class*=TLStatsTopThreeHeader')
        categories = zip(category_names, category_links)
        logger.info(f"Found {len(category_links)} links and {len(category_names)} names")
        print(category_links)
        for category in categories:
            logger.info(f"Visiting {category[1]}")
            collect(driver, category[0].text, category[1])
    finally:
        logger.info("Closing driver")
        driver.quit()

def collect(driver, category, link):
    driver.get(link)
    #players = driver.find_elements(By.CSS_SELECTOR, 'div[class*=LeagueSeasonStatsTableCSS a')
    with open('test.txt', 'w') as f:
        f.write(20*'=' f" {category} " + 20*'=' + "\n")

        names = driver.find_elements(By.CSS_SELECTOR, 'span[class*=TeamOrPlayerName')
        values = driver.find_elements(By.CSS_SELECTOR, 'span[class*=StatValue')

        logger.info(f"Category={category} | players={len(names)} | values={len(values)}")

        for i in range(len(names)):
            f.write(f"{names[i].text}; {values[i].text}\n")

def main():
    logging.basicConfig(level=logging.INFO)

    crawl(SOURCE+STATS_PAGE)

if __name__ == '__main__':
    main()