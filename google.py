from selenium import webdriver
from bs4 import BeautifulSoup as soups
import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def search_selenium(search_name, search_limit):
    search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
    browser = webdriver.Chrome('C:/GitHub/wa/chromedriver.exe')
    browser.get(search_url)
    image_count = len(browser.find_elements_by_tag_name("img"))
    browser.implicitly_wait(2)  # data가 load될 때까지 2초간 기다려 준다.
    image_save_folder = f"c:/data/Chrome Images/{search_name}/"
    createFolder(image_save_folder)
    for i in range(search_limit + 30):
        if i < 30:  # top 30개 이미지 skip (검색어와 무관함)
            continue
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot(image_save_folder + str(i - 29) + ".png")


#     browser.close()
if __name__ == "__main__":
    search_name = input("검색하고 싶은 키워드 : ")
    search_limit = int(input("원하는 이미지 수집 개수 : "))
    search_path = "Your Path"
    search_selenium(search_name, search_limit)
