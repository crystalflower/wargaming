import random
from typing import List, Dict


def field_generator(number_of_columns: int, number_of_lines: int) -> List[List[int]]:
    # Генерируем поле только с нулями (водой)
    field = [[0 for _ in range(number_of_columns)] for _ in range(number_of_lines)]

    count_of_land = number_of_columns * number_of_lines * 30 // 100

    # В случайном порядке добавляем единицы на поле (сушу)
    while count_of_land:
        x_coordinate = random.randint(0, number_of_lines - 1)
        y_coordinate = random.randint(0, number_of_columns - 1)

        if field[y_coordinate][x_coordinate]:
            continue
        else:
            field[y_coordinate][x_coordinate] = 1

            count_of_land -= 1

    return field


# Проверяем связи вокруг элементов в порядке: вверх, вниз, влево, вправо,
# если соседний элемент ноль (вода), добавляем его в доступные координаты для перехода
def graph_generator(field: List[List[int]]) -> Dict[tuple, List]:
    graph = {}
    max_index = len(field) - 1

    for y_index, row in enumerate(field):
        for x_index, value in enumerate(row):
            connections = []
            if value == 0:
                if y_index > 0:
                    element = field[y_index - 1][x_index]
                    if element == 0:
                        connections.append((x_index, y_index - 1))
                if y_index < max_index:
                    element = field[y_index + 1][x_index]
                    if element == 0:
                        connections.append((x_index, y_index + 1))
                if x_index > 0:
                    element = field[y_index][x_index - 1]
                    if element == 0:
                        connections.append((x_index - 1, y_index))
                if x_index < max_index:
                    element = field[y_index][x_index + 1]
                    if element == 0:
                        connections.append((x_index + 1, y_index))

            graph[(x_index, y_index)] = connections

    return graph
