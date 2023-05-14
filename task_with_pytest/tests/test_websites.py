from task_with_pytest.pages import WebsitesProgrammingLanguagesPage
import pytest

websites_programming_languages_data = None


@pytest.mark.parametrize(
    'default_popularity',
    [
        10 ** 7,
        int(1.5 * (10 ** 7)),
        5 * (10 ** 7),
        10 ** 8,
        5 * (10 ** 8),
        10 ** 9,
        int(1.5 * (10 ** 9))
    ]
)
def test_popularity_check(
        init_browser,
        default_popularity
):
    # Храним данные в виде глобальной переменной, если переиспользование подразумевается в текущем файле тестов
    # Возможна реализация получения данных в фикстуре и использование их на протяжении всей сессии без привязки к файлу
    global websites_programming_languages_data

    page = WebsitesProgrammingLanguagesPage(init_browser)
    websites_programming_languages_data = page.get_data_from_websites_languages_table()

    assert_results = []

    for website in websites_programming_languages_data:
        try:
            assert website.popularity > default_popularity, \
                f'{website.websites} (Frontend:{website.frontend}|Backend:{website.backend}) has ' \
                f'{website.popularity} unique visitors per month. (Expected more than {default_popularity})'
        except AssertionError as assertion:
            assert_results.append(str(assertion))

    if assert_results:
        pytest.fail('\n'.join(assert_results))
