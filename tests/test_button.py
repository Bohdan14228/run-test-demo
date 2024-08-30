from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    у = 0
    return chrome_browser


def test_button_exist(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    assert browser.find_element('id', 'submit-id-submit').is_displayed()