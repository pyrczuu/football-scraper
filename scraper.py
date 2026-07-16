import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

load_dotenv()
logger = logging.getLogger()


# ---------- INDIVIDUAL STATS ---------- #

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
        elements = driver.find_elements(By.CSS_SELECTOR, 'h3[class*=TLStatsTopThreeHeader')
        category_names = [el.text for el in elements]
        categories = zip(category_names, category_links)
        logger.info(f"Found {len(category_links)} links and {len(category_names)} names")
        print(category_links)
        for category in categories:
            logger.info(f"Visiting {category[1]}")
            collect(driver, category[0], category[1])
    finally:
        logger.info("Closing driver")
        driver.quit()

def collect(driver, category, link):
    driver.get(link)
    with open('test.txt', 'a') as f:
        f.write(f"{20*'='} {category} {20*'='}\n")

        wait = WebDriverWait(driver, 5)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class*=TeamOrPlayerName')))

        names = driver.find_elements(By.CSS_SELECTOR, 'span[class*=TeamOrPlayerName')
        values = driver.find_elements(By.CSS_SELECTOR, 'span[class*=StatValue')

        logger.info(f"Category={category} | players={len(names)} | values={len(values)}")

        for i in range(len(names)):
            f.write(f"{names[i].text}; {values[i].text}\n")

# ---------- TODO PLAYER PROFILES ---------- #