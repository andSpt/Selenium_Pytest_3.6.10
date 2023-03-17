import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_basket(browser):
    browser.get(link)
    time.sleep(30)
    button_add_basket = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")


