from bs4 import BeautifulSoup
from selenium import webdriver
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
        time.sleep(5)
        with open("index_selenium.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_data("https://yandex.ru/images/search?text=tiger")

if __name__ == "__main__":
    main()