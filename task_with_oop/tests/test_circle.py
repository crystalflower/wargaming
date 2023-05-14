import pytest

from task_with_oop.shapes import CircleShape


class TestCircle:
    @pytest.mark.parametrize(
        'start_x, start_y, radius',
        [
            (0, 0, 1),
            (0, 0, 0.5)
        ]
    )
    def test_correct_radius(self, start_x, start_y, radius):
        test_circle = CircleShape(start_x, start_y, radius)

        assert isinstance(test_circle, CircleShape), 'Circle has not been initialized'

    @pytest.mark.parametrize(
        'start_x, start_y, radius',
        [
            (0, 0, 0),
            (0, 0, -1),
            (0, 0, -1.1)
        ]
    )
    def test_incorrect_radius(self, start_x, start_y, radius):
        try:
            CircleShape(start_x, start_y, radius)
        except AssertionError:
            pass
        else:
            raise AssertionError(f'No check for invalid radius value - {radius}')

    @pytest.mark.parametrize(
        'start_x, start_y, radius',
        [
            ('string', 'string', 'string'),
            (None, None, None),
            (True, False, True),
            (1.1, 1.1, 1.1),
            (1, 1, 'string'),
            (1, 1, None),
            (1, 1, bool),
            (list(), list(), list()),
            (1, 1, list())
        ]
    )
    def test_incorrect_datatypes_for_circle(self, start_x, start_y, radius):
        try:
            CircleShape(start_x, start_y, radius)
        except TypeError:
            pass
        else:
            raise AssertionError(f'No check for incorrect data type')
