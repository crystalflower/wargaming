from pytest import fixture
from selenium import webdriver


@fixture
def init_browser():
    """Инициализация браузера"""
    browser_session = webdriver.Chrome()

    yield browser_session

    browser_session.quit()
