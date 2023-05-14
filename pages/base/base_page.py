from typing import List

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import settings


class BasePage:
    # Передаем экземпляр браузера из фикстуры при инициализации объекта страницы,
    # а также ожидаем загрузку и проверяем корректность URLа
    def __init__(
            self,
            app,
            is_loaded=True,
            wait_url_timeout=settings.SMALL_TIMEOUT
    ):
        self.app = app
        self.open_page_and_check(self.base_url, is_loaded, wait_url_timeout)

    @property
    def base_url(self) -> str:
        return ''

    def is_url_correct(self, url: str, timeout: int = settings.SMALL_TIMEOUT) -> bool:
        try:
            WebDriverWait(self.app, timeout).until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def open_page(self, url: str):
        self.app.get(url)

    @property
    def current_url(self):
        return self.app.execute('getCurrentUrl')['value']

    def open_page_and_check(
            self,
            url: str,
            is_loaded: bool = True,
            wait_url_timeout: int = settings.SMALL_TIMEOUT
    ):
        self.open_page(url)

        assert self.is_url_correct(url, wait_url_timeout),\
            f'Current url must be "{url}", but still "{self.current_url}"'

        if is_loaded:
            self.is_loaded()

    # Проверяем загрузку страницы с помощью JS
    def is_loaded(self, timeout: int = settings.DEFAULT_PERFORMANCE_TIMEOUT) -> bool:
        try:
            WebDriverWait(self.app, timeout).until(
                lambda _: self.app.execute_script('return document.readyState') == 'complete'
            )
            return True
        except TimeoutException:
            return False

    def find_elements(self, by: str, loc: str) -> List[WebElement]:
        return self.app.find_elements(by, loc)

    def get_text_from_elements(self, by: str, loc: str) -> List[str]:
        elements = self.find_elements(by, loc)
        return [element.get_attribute('innerText') for element in elements]
