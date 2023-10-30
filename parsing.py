from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os



def get_data(request):
    url = f"https://yandex.ru/images/search?text={request}"
    os.mkdir(f"dataset/{request}")
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "cache-control":"private, max-age=3600",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
    }
    driver = webdriver.Firefox()
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(3)

    with open(f"urls_{request}.txt", 'w') as file:  #скачивание ссылок
        for i in range(0,1500):
            time.sleep(0.05)
            #driver.find_element(By.CSS_SELECTOR, "a.Button2_view_action").click() #открыть фотку

            link = driver.find_element(By.CSS_SELECTOR,"a.Button2_view_action").get_attribute("href")
            print(i)
            file.write(link + '\n')
            #iter+=1
            driver.find_element(By.CSS_SELECTOR, "div.CircleButton:nth-child(4)").click() #следующая фотка
 
    driver.close()
    driver.quit()

def get_links(request):
    iter = 586
    i = 1
    with open(f"urls_{request}.txt", "r") as file:
        for line in file:
            url = line.strip()
            if iter<i:
                time.sleep(1)
                response = requests.get(url, verify=False)
                if response.status_code == 200:
                    with open(f"{request}/{iter}.jpg", "wb") as image_file:
                        image_file.write(response.content)
                    print(f'{iter} успешно скачано.')
                    iter+=1
                else:
                    print(f'Ошибка при скачивании изображения с URL: {url}')
            print(i)
            i+=1


def main():
    #get_data("leopard")
    get_links("tiger")

if __name__ == "__main__":
    main()