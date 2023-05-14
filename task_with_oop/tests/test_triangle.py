import pytest

from task_with_oop.shapes import TriangleShape


class TestTriangle:
    @pytest.mark.parametrize(
        'first_x, first_y, second_x, second_y, third_x, third_y',
        [
            (0, 0, 3, 0, 0, 4),
            (1, 1, 5, 1, 3, 5),
            (-2, 0, 2, 0, 0, 3)
        ]
    )
    def test_correct_coordinates_for_triangle(self, first_x, first_y, second_x, second_y, third_x, third_y):
        test_triangle = TriangleShape(first_x, first_y, second_x, second_y, third_x, third_y)

        assert isinstance(test_triangle, TriangleShape), 'Triangle has not been initialized'

    @pytest.mark.parametrize(
        'first_x, first_y, second_x, second_y, third_x, third_y',
        [
            (0, 0, 0, 0, 0, 0),
            (0, 0, 1, 1, 2, 2)
        ]
    )
    def test_incorrect_coordinates_for_triangle(self, first_x, first_y, second_x, second_y, third_x, third_y):
        try:
            TriangleShape(first_x, first_y, second_x, second_y, third_x, third_y)
        except AssertionError:
            pass
        else:
            raise AssertionError('No check for invalid coordinates value')

    @pytest.mark.parametrize(
        'first_x, first_y, second_x, second_y, third_x, third_y',
        [
            ('string', 'string', 'string', 'string', 'string', 'string'),
            (None, None, None, None, None, None),
            (True, False, True, True, False, False),
            (1.1, 1.1, 1.1, 1.1, 1.1, 1.1),
            (1, 1, 'string', 1, 1, 1),
            (1, 1, 1, 1, 1, None),
            (1, 1, 1, bool, 1, 1),
            (list(), list(), list(), list(), list(), list()),
            (1, 1, list(), 1, 1, 1)
        ]
    )
    def test_incorrect_datatypes_for_triangle(self, first_x, first_y, second_x, second_y, third_x, third_y):
        try:
            TriangleShape(first_x, first_y, second_x, second_y, third_x, third_y)
        except TypeError:
            pass
        else:
            raise AssertionError(f'No check for incorrect data type')
