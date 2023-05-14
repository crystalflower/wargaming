from typing import List

from task_with_pytest import settings
from task_with_pytest.builtin_types.datacontainers import WebsiteProgrammingLanguages
from task_with_pytest.locators import WebsitesProgrammingLanguagesLocators
from task_with_pytest.pages.base import BasePage
from task_with_pytest.utils import reformat_header, clear_data_from_links, num_from_fstring


class WebsitesProgrammingLanguagesPage(BasePage):
    base_url = settings.WEBSITES_PROGRAMMING_LANGUAGES_URL

    def get_data_from_websites_languages_table(self) -> List[WebsiteProgrammingLanguages]:
        # Получаем данные из заголовков столбцов таблицы и строк
        headers_of_table = self.get_text_from_elements(*WebsitesProgrammingLanguagesLocators.WEBSITES_TABLE_HEADERS)
        rows_of_table = self.get_text_from_elements(*WebsitesProgrammingLanguagesLocators.WEBSITES_TABLE_ROWS)

        data_from_website_table = []

        for data_row in rows_of_table:
            # Получаем совпадающий с заголовками список строки
            list_of_data = data_row.split('\t')

            dict_of_data = {}

            for index, header in enumerate(headers_of_table):
                clean_header = reformat_header(header)
                clean_value = clear_data_from_links(list_of_data[index])

                if clean_header == settings.POPULARITY:
                    dict_of_data[clean_header] = num_from_fstring(clean_value)
                else:
                    dict_of_data[clean_header] = clean_value

            # Преобразуем обработанный словарь в класс данных для удобного использования
            data_from_website_table.append(WebsiteProgrammingLanguages(**dict_of_data))

        return data_from_website_table
