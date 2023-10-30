from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "cache-control":"private, max-age=3600",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
    }

def get_data(url):
    try:
        driver=webdriver.Firefox()

        driver.get(url=url)
        driver.maximize_window()
        time.sleep(1)

    #     flag = driver.find_element(By.CLASS_NAME, "button2__text")
    #     driver.find_element("span class="button2__text">Ещё картинки</span>")
    #     driver.execute_script("argument[0].scrollIntoView();", flag)

        for j in range(1,10):
            for i in range(1,10):
                driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                time.sleep(0.5)
            button = driver.find_element(By.CSS_SELECTOR, ".button2").click()

        with open("index_selenium.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        time.sleep(10)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_data("https://yandex.ru/images/search?text=tiger")

if __name__ == "__main__":
    main()

