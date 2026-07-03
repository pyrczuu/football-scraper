import os
from dotenv import load_dotenv
from pandas.core.interchange.dataframe_protocol import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

load_dotenv()


def crawl(path: str):
    driver = webdriver.Chrome()

    driver.get(path)
    try:
        categoryLinks = driver.find_elements(By.CSS_SELECTOR, 'div[class*="TLStatsTopThreeHeader"] a')
        categoryNames = driver.find_elements(By.CSS_SELECTOR, 'h3[class*=TLStatsTopThreeHeader')
        categories = zip(categoryNames, categoryLinks)
        for category in categories:
            collect(driver, category[0], category[1])
    finally:
        driver.quit()

def collect(driver, name, link):
    driver.get(link)
    players = driver.find_elements(By.CSS_SELECTOR, 'div[class*=LeagueSeasonStatsTableCSS a')
    for player in players:
        name = driver.find_element(By.CSS_SELECTOR, 'span[class*=TeamOrPlayerName')
        value = driver.find_element(By.CSS_SELECTOR, 'span[class*=StatValue')
        # add saving logic, probably straight to postgres, no excel as middle man
def main():
    SOURCE = os.getenv("SOURCE")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH")

    crawl(SOURCE)

if __name__ == '__main__':
    main()