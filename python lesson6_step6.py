from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("test")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    driver.close()
    time.sleep(30)
    driver.quit()