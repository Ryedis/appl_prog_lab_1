import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data(request) -> None :
    url = f"https://yandex.ru/images/search?text={request}"
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "cache-control":"private, max-age=3600",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
    }
    driver = webdriver.Firefox()
    driver.get(url = url)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'div.serp-item__preview a.serp-item__link').click()

    with open(f"urls_{request}.txt", 'w') as file:
        for i in range(0, 6):
            time.sleep(0.05)
            link = driver.find_element(By.CSS_SELECTOR, "a.Button2_view_action").get_attribute("href")
            print(i)
            file.write(link + '\n')
            driver.find_element(By.CSS_SELECTOR, "div.CircleButton:nth-child(4)").click()

    driver.close()
    driver.quit()


def get_links(request) -> None :
    count = 0
    os.mkdir(os.path.join("dataset", request))

    with open(os.path.join("urls_", request, ".txt"), "r") as file:
        for line in file:
            try:
                url = line.strip()
                time.sleep(1)
                response = requests.get(url)
                if response.status_code == 200:
                    with open(os.path.join("dataset/", request, '/', count, ".jpg"), "wb") as image_file:
                        image_file.write(response.content)
                    print(f'{count} успешно скачано')
                    count+=1
                else:
                    print(f'Ошибка при скачивании изображения с URL: {url}')
            except:
                continue


def rename_files(request) -> None :
    folder_path = os.path.join("dataset", request)
    count = 0

    for filename in os.listdir(folder_path):
        old_file_path = os.path.join(folder_path, filename)
        number = str(count)
        new_filename = number.zfill(4) + ".jpeg"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print (f"{count} переименовано")
        count += 1


def main() -> None :
    request = input("Введите запрос: ")
    get_data(request)
    get_links(request)
    rename_files(request)


if __name__ == "__main__":
    main()