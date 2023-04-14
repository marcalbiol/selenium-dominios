import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def print_hi():
    global href
    hrefs = []
    URL = "https://random-word-api.herokuapp.com/all"
    r = requests.get(url=URL)
    data = r.json()

    driver = webdriver.Chrome()
    time.sleep(3)
    driver.get("https://www.google.com")
    cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@id= "L2AGLb"]'))
    )
    cookies.click()

    for x in data:
        time.sleep(2)
        inputGoogle = driver.find_element(By.XPATH, "//textarea[@title = \"Buscar\"]")
        inputGoogle.clear()
        inputGoogle.send_keys(x)
        inputGoogle.send_keys(Keys.ENTER)
        time.sleep(3)
        print('palabra ' + x)
        for r in range(1, 9):
            try:
                print(driver.find_element(By.XPATH,
                                          f"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[{r}]/div/div"
                                          f"/div[1]/div/a").get_attribute(
                    "href"))
            except NoSuchElementException:
                pass
         # hrefs.append(href)
        driver.back()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
