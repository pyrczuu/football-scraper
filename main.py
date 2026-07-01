import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()


def crawl(path: str):
    driver = webdriver.Chrome()
    stats_container = 'section[class*="TLStatsPageCSS"]'

    driver.get(path)
    try:
        stats = driver.find_element(By.CSS_SELECTOR, 'section[class*="TLStatsPageCSS"]')
    finally:
        driver.quit()

def collect():
    pass

def main():
    SOURCE = os.getenv("SOURCE")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH")

    crawl(SOURCE)

if __name__ == '__main__':
    main()