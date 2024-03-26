import logging
import yaml

from testPage import OperationsHelper
with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# WEB TESTS

# проверка валидной авторизации
def test_step_1(browser):
    logging.info("Test-1 start: проверка валидной авторизации")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_hello_user() == f'Hello, {testdata["login"]}'


# проверка перехода по кнопке about на страницу About Page
def test_step_2(browser):
    logging.info("Test-2 start: проверка перехода по кнопке about на страницу About Page")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_about_btn()
    assert testpage.get_title_about_text() == "About Page"


# проверка размера шрифта заголовка страницы About Page
def test_step_3(browser):
    logging.info("Test-3 start: проверка размера шрифта заголовка страницы About Page")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_about_btn()
    assert testpage.get_size_font_about() == '32px'
