from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)
    # browser.implicitly_wait(5)
    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button_add_to_basket) == 1, "Button 'add to basket' missing"

