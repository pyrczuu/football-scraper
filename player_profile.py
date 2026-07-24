import re

from selenium.webdriver.common.by import By


def save_if_absent(connection, driver, logger, url: str):
    player_id = re.search(r'/players/(\d+)', url)
    player_name = driver.find_element(By.CSS_SELECTOR, 'h1[class*=PlayerNameCSS]').text.strip()
    player_club = driver.find_element(By.CSS_SELECTOR, 'div[class*=TeamCSS]').text.strip()
    player_nation = driver.find_element(By.CSS_SELECTOR, 'a[class*=CountryLinkCSS]').text.strip()
    player_age = "" #TODO, tricky, maybe findselemnts and get by index from list
    player_position = driver.find_element(By.CSS_SELECTOR, 'div[class*=PositionCSS]').text.strip()
    player_value = ""  #TODO

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM players WHERE id = (%d);"
        cursor.execute(query, player_id)
        rows = cursor.fetchall()

        if len(rows) == 0:
            pass # TODO post player data

        cursor.close()

    except Exception as error:
        logger.info(f"Error fetching data: {error}")