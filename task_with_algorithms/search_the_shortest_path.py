import collections
from typing import Dict, List

from utils import field_generator, graph_generator

number_of_lines = int(input('Enter the number of field lines: '))
number_of_columns = int(input('Enter the number of field columns: '))

start_position = (int(input("Enter x coordinate for A position: ")), int(input("Enter y coordinate for A position: ")))

end_position = (int(input("Enter x coordinate for B position: ")), int(input("Enter y coordinate for B position: ")))

field = field_generator(number_of_columns, number_of_lines)
graph_coordinates_connections = graph_generator(field)

for row in field:
    print(row)


def search_the_shortest_path(graph_for_search: Dict[tuple, List], start_pos: tuple, end_pos: tuple) -> str:
    if start_pos not in graph_for_search or end_pos not in graph_for_search:
        return 'You entered incorrect coordinates, origin of coordinates is considered from 0 to the maximum value - 1.'

    if start_pos == end_pos:
        return 'You entered the same coordinates, movement is impossible'

    search_queue = collections.deque()
    search_queue.append(start_pos)

    ancestors = {start_pos: None}

    while search_queue:
        coordinates = search_queue.popleft()

        if coordinates == end_pos:
            break

        # Проходимся по доступным координатам перехода, записываем текущую координату как предшествующую доступной
        for connection in graph_for_search[coordinates]:
            if connection not in ancestors:
                search_queue.append(connection)
                ancestors[connection] = coordinates
    else:
        return f'The path from coordinate {start_position} to coordinate {end_position} is impossible'

    path = []
    coordinates = end_pos
    while coordinates is not None:
        # Получаем кратчайший путь по связям предшествующих координат
        path.insert(0, coordinates)
        coordinates = ancestors[coordinates]

    path = ' -> '.join((map(str, path)))
    return f'The shortest path from coordinate {start_position} to coordinate {end_position}:\n{path}'


searched_result = search_the_shortest_path(graph_coordinates_connections, start_position, end_position)

print(searched_result)
