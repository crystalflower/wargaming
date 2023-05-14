from task_with_oop.shapes.base import BaseShape


class RectangleShape(BaseShape):
    def __init__(
            self,
            first_x: int,
            first_y: int,
            second_x: int,
            second_y: int
    ):
        is_first_x_int = type(first_x) == int
        is_first_y_int = type(first_y) == int
        is_second_x_int = type(second_x) == int
        is_second_y_int = type(second_y) == int

        if not is_first_x_int or not is_first_y_int or not is_second_x_int or not is_second_y_int:
            raise TypeError('Invalid data type')

        assert first_x != second_x and first_y != second_y, 'Coordinates cannot lie on the same axis'

        super().__init__(first_x, first_y)

        self.second_x = second_x
        self.second_y = second_y

    def draw(self, colour: str = None):
        text_result = f'Drawing Rectangle:({self.first_x}, {self.first_y}) with coordinate ({self.second_x}, ' \
                      f'{self.second_y}).'

        if colour:
            text_result = '{} {}'.format(text_result, f'Colour {colour}.')

        print(text_result)
