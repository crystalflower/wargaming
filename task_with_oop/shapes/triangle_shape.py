from task_with_oop.shapes.base import BaseShape
from task_with_oop.utils import are_triangle_points_collinear


class TriangleShape(BaseShape):
    def __init__(
            self,
            first_x: int,
            first_y: int,
            second_x: int,
            second_y: int,
            third_x: int,
            third_y: int,
    ):
        is_first_x_int = type(first_x) == int
        is_first_y_int = type(first_y) == int
        is_second_x_int = type(second_x) == int
        is_second_y_int = type(second_y) == int
        is_third_x_int = type(third_x) == int
        is_third_y_int = type(third_y) == int

        if not is_first_x_int or not is_first_y_int or not is_second_x_int or not is_second_y_int \
                or not is_third_x_int or not is_third_y_int:
            raise TypeError('Invalid data type')

        first_not_equal_second = (first_x, first_y) != (second_x, second_y)
        first_not_equal_third = (first_x, first_y) != (third_x, third_y)
        second_not_equal_third = (second_x, second_y) != (third_x, third_y)

        assert first_not_equal_second and first_not_equal_third and second_not_equal_third, 'Coordinates must be unique'

        assert not are_triangle_points_collinear(first_x, first_y, second_x, second_y, third_x, third_y), \
            'Coordinates lie on the same line'

        super().__init__(first_x, first_y)

        self.second_x = second_x
        self.second_y = second_y
        self.third_x = third_x
        self.third_y = third_y

    def draw(self, colour: str = None):
        text_result = f'Drawing Triangle:({self.first_x}, {self.first_y}) with coordinates ' \
                      f'({self.second_x}, {self.second_y}), ({self.third_x}, {self.third_y}).'

        if colour:
            text_result = '{} {}'.format(text_result, f'Colour {colour}.')

        print(text_result)
