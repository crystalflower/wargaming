import pytest

from task_with_oop.shapes import RectangleShape


class TestRectangle:
    @pytest.mark.parametrize(
        'first_x, first_y, second_x, second_y',
        [
            (0, 0, 1, 1),
            (1, 1, -4, -2)
        ]
    )
    def test_correct_coordinates_for_rectangle(self, first_x, first_y, second_x, second_y):
        test_rectangle = RectangleShape(first_x, first_y, second_x, second_y)

        assert isinstance(test_rectangle, RectangleShape), 'Rectangle has not been initialized'

    @pytest.mark.parametrize(
        'first_x, first_y, second_x, second_y',
        [
            (0, 0, 0, 0),
            (1, 1, 1, 2),
            (0, 1, 3, 1)
        ]
    )
    def test_incorrect_coordinates_for_rectangle(self, first_x, first_y, second_x, second_y):
        try:
            RectangleShape(first_x, first_y, second_x, second_y)
        except AssertionError:
            pass
        else:
            raise AssertionError('No check for invalid coordinates value')

    @pytest.mark.parametrize(
        'first_x, first_y, second_x, second_y',
        [
            ('string', 'string', 'string', 'string'),
            (None, None, None, None),
            (True, False, True, True),
            (1.1, 1.1, 1.1, 1.1),
            (1, 1, 'string', 1),
            (1, 1, 1, None),
            (1, 1, 1, bool),
            (list(), list(), list(), list()),
            (1, 1, list(), 1)
        ]
    )
    def test_incorrect_datatypes_for_rectangle(self, first_x, first_y, second_x, second_y):
        try:
            RectangleShape(first_x, first_y, second_x, second_y)
        except TypeError:
            pass
        else:
            raise AssertionError(f'No check for incorrect data type')
