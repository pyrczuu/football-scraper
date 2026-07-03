import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()


def crawl(path: str):
    driver = webdriver.Chrome()

    driver.get(path)
    try:
        categoryLinks = driver.find_elements(By.CSS_SELECTOR, 'div[class*="TLStatsTopThreeHeader"] a')
        categoryNames = driver.find_elements(By.CSS_SELECTOR, 'h3[class*=TLStatsTopThreeHeader')
        categories = zip(categoryNames, categoryLinks)
        for category in categories:
            collect(category[0], category[1])
    finally:
        driver.quit()

def collect(name, link):
    pass

def main():
    SOURCE = os.getenv("SOURCE")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH")

    crawl(SOURCE)

if __name__ == '__main__':
    main()