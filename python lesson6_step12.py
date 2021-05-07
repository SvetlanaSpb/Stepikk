from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc():
        return str(int(x) + int(z))
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    z_element = browser.find_element_by_id("num2")
    z = z_element.text
    print (x,z)

    x2 = str(int(x) + int(z))

    option = browser.find_element_by_id("dropdown")
    option.click()

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


