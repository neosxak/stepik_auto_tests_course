from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math, time, os
"""
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха 
по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене 
объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 
12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и 
отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод 
text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в 
качестве ответа на это задание.
"""
def calc(x):
    return math.log(abs(12*math.sin(x)))

browserCloseDelay = 3
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)


try:
    # замена sleep говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    # button = WebDriverWait(browser, 12).until(
    #     EC.element_to_be_clickable((By.ID, "book"))
    # )
    # text_el = browser.find_element(By.ID, 'price').text
    # tmp = ""
    # while text_el != '$100':
    #     text_el = browser.find_element(By.ID, 'price').text
    #     if tmp != text_el:
    #         #print(text_el)
    #         tmp = text_el
    #     if text_el == '$100':
    #         button.click()
    #         x = int(browser.find_element(By.ID, 'input_value').text)
    #         browser.find_element(By.ID, 'answer').send_keys(calc(x))
    #         browser.find_element(By.ID, 'solve').click()
    #         time.sleep(5)
    #         break
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element(By.ID, "book").click()
    num = browser.find_element(By.ID, "input_value")
    res = calc(int(num.text))

    browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(browserCloseDelay)
    # закрываем браузер после всех манипуляций
    browser.quit()
