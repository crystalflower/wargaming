from typing import Union

from task_with_oop.shapes.base import BaseShape


class CircleShape(BaseShape):
    def __init__(
            self,
            first_x: int,
            first_y: int,
            radius: Union[int, float]
    ):
        is_first_x_int = type(first_x) == int
        is_first_y_int = type(first_y) == int
        is_radius_int_or_float = type(radius) == int or type(radius) == float

        if not is_first_x_int or not is_first_y_int or not is_radius_int_or_float:
            raise TypeError('Invalid data type')

        assert radius > 0, 'Circle cannot be zero or negative radius'

        super().__init__(first_x, first_y)

        self.radius = radius

    def draw(self, colour: str = None):
        text_result = f'Drawing Circle:({self.first_x}, {self.first_y}) with radius {self.radius}.'

        if colour:
            text_result = '{} {}'.format(text_result, f'Colour {colour}.')

        print(text_result)
