import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://ya.ru/"

browser = webdriver.Chrome()
browser.get(link)
first_page = browser.current_url


def Serchstring():
    # Ищу строку
    Check_serch_line = WebDriverWait(browser, 8).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class*=search3__input]")))
    serch_string = browser.find_element(By.CSS_SELECTOR, "input[class*=search3__input]").click()
    first_page = browser.title


def input_word():
    serch_string = browser.find_element(By.CSS_SELECTOR, "input[class*=search3__input]")
    serch_string.send_keys("Тензор")


def Check_minisugest():
    minisugest = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class*=mini-suggest__popup-content]")))
    serch_sugest = browser.find_element(By.CSS_SELECTOR, "ul[class*=mini-suggest__popup-content]")
    assert serch_sugest != None, "Таюлица с подсказками не найдена"


def press_enter():
    serch_string = browser.find_element(By.CSS_SELECTOR, "input[class*=search3__input]")
    serch_string.send_keys(Keys.ENTER)
    assert browser.current_url != first_page, "Страница не найдена"


def Check_first_link():
    # проверка на прогрузку страницы поиска
    first_link = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class*=Link_theme_normal]")))
    check_link_tensor = browser.find_element(By.LINK_TEXT, "tensor.ru")
    assert check_link_tensor.text == "tensor.ru", "1 ссылка не ведет на https://tensor.ru/"


def check_menu():
    search_menu = browser.find_element(By.CSS_SELECTOR, "div[class*=services-suggest__icons-more]")
    assert search_menu != None, "Menu is no found"
    search_menu.click()


def clickbuttun():
    btn = browser.find_element(By.CSS_SELECTOR, "a[aria-label*=Картинки]")
    btn.click()
    assert btn.text == "Картинки", "Кнопка не найдена"


def swich_window():
    for handle in browser.window_handles:
        browser.switch_to.window(handle)


def check_url():
    assert browser.current_url == "https://ya.ru/images/", "Вы перешли не по ссылке https://yandex.ru/images/"


def find_and_click_first_img():
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=PopularRequestList-Item_pos_0]"))
    )
    find_img = browser.find_element(By.CSS_SELECTOR, "div[class*=PopularRequestList-Item_pos_0]")
    find_img.click()


def check_input_line_group():
    line_input = browser.find_element(By.CSS_SELECTOR, "input[class*=mini-suggest__input]")
    assert line_input != None, "Срока поиска пуста"


def click_img():
    IMG = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=serp-item_type_search]"))
    )
    first_img = browser.find_element(By.CSS_SELECTOR, "div[class*=serp-item_type_search]")
    first_img.click()
    assert first_img != None, "Картинка не открылась"


def check_open_img():
    check_img = browser.find_element(By.CSS_SELECTOR, "img[class*=MMImage-Origin]")
    assert check_img != None, "Error: картинка не открылась"
    return check_img.get_attribute('src')


def button_next():
    btn_next = browser.find_element(By.CSS_SELECTOR, "div[class*=CircleButton_type_next]").click()


def check_change_img(first, second):
    assert first != second, "Картинка не сменилась"


def press_button_back():
    btn_back = browser.find_element(By.CSS_SELECTOR, "div[class*=CircleButton_type_prev]").click()


def check_first_img(second):
    IMG = browser.find_element(By.CSS_SELECTOR, "img[class*=MMImage-Origin]")
    print(IMG.get_attribute('src'))
    assert IMG.get_attribute('src') != second, "Картинка не вернулась"


# Задание 1
Serchstring()
input_word()
Check_minisugest()
press_enter()
Check_first_link()

# Задание2
browser.get(link)
Serchstring()
check_menu()
clickbuttun()
swich_window()

check_url()
find_and_click_first_img()
check_input_line_group()
click_img()
first_img = check_open_img()
button_next()
second_img = check_open_img()
check_change_img(first_img, second_img)
press_button_back()

print(first_img)
print(second_img)
check_first_img(second_img)

browser.quit()

if __name__ == "main":
    pytest.main()
