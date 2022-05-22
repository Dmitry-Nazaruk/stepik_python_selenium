from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element_by_id("treasure")
    box_value = box.get_attribute("valuex")
    result = calc(box_value)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(result)
    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()
    time.sleep(3)
    input3 = browser.find_element_by_id('robotsRule')
    input3.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()