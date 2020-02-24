# Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language

import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language: en, ru, ... (etc.)')

@pytest.fixture(scope='function')
def browser(request):
    
    user_language = request.config.getoption("language")
    
    # options = Options
    options = webdriver.ChromeOptions()
    
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    print('\nstart Chrome browser..')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser..')
    browser.quit()
