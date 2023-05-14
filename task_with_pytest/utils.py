import re


# Форматируем строку для параметра класса данных
def reformat_header(title: str) -> str:
    return title.split('\n')[0].lower().replace('-', '')


# Убираем сслыки в квадратных скобках из текста
def clear_data_from_links(data: str) -> str:
    return re.sub(r'\[\d+\]', '', data)


# Преобразуем строку с лишними символами в число
def num_from_fstring(fstring):
    num = re.sub(r'\D', '', fstring)
    return int(num)
