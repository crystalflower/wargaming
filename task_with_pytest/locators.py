from selenium.webdriver.common.by import By


# Описываем класс локаторов для удобства хранения
class Locator:
    def __init__(self, by, locator, description):
        self.by = by
        self.description = description
        self.locator = locator

    def __iter__(self):
        return iter((self.by, self.locator))


class WebsitesProgrammingLanguagesLocators:
    WEBSITES_TABLE_HEADERS = Locator(
        By.XPATH, '//table[caption[contains(text(), "Programming")]]//th', description='Заголовки столбцов таблицы'
    )
    WEBSITES_TABLE_ROWS = Locator(
        By.XPATH, '//table[caption[contains(text(), "Programming")]]//tbody/tr', description='Строки таблицы'
    )
