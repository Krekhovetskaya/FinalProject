from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import yaml
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    url = testdata["address"]



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = url


    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        except:
            logging.exception(('Find element exception'))
            element = None
        return element


    def get_element_property(self, locator, property):       # получение свойства элемента (например получение цвета кнопки)
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)          # получение свойства у элемента, если свойство есть
        else:
            logging.exception(f'Property {property} not found in element with {locator}')
            return None


    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing
