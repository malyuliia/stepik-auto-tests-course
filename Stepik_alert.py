from selenium import webdriver
import time
import math
import os
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element_by_css_selector("button[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value")
    x1 = x.text
    y = calc(x1)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button_2 = browser.find_element_by_css_selector("button[type='submit']").click()






finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()