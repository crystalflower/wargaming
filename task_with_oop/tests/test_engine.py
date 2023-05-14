from task_with_oop.engine import Engine2D
from task_with_oop.shapes import TriangleShape, RectangleShape, CircleShape


class TestEngine:
    def test_positive_draw(self, capsys):
        engine = Engine2D()

        circle = CircleShape(0, 0, 1)
        triangle = TriangleShape(0, 0, 3, 0, 0, 4)
        rectangle = RectangleShape(0, 0, 1, 1)

        engine.add_shapes_to_canvas([circle, triangle, rectangle])

        engine.draw()

        captured = capsys.readouterr()

        assert 'Circle' in captured.out, 'The circle was not drawn'
        assert 'Triangle' in captured.out, 'The triangle was not drawn'
        assert 'Rectangle' in captured.out, 'The rectangle was not drawn'

        assert not engine._canvas, 'Canvas must be cleared'

    def test_change_colour(self, capsys):
        colour = 'green'

        engine = Engine2D()

        first_shape = CircleShape(0, 0, 1)
        second_shape = CircleShape(0, 0, 1)

        engine.add_shapes_to_canvas([first_shape, second_shape])
        engine.change_colour(colour)

        engine.draw()

        captured = capsys.readouterr()

        assert colour in captured.out, 'The colour was not changed'

    def test_add_not_shape_to_canvas(self):
        engine = Engine2D()

        try:
            engine.add_shapes_to_canvas('not shape')
        except AssertionError:
            pass
        else:
            raise AssertionError('No check for passing the data type of the shape')

    def test_empty_canvas(self):
        engine = Engine2D()

        try:
            engine.draw()
        except AssertionError:
            pass
        else:
            raise AssertionError('No validation to empty canvas')

    def test_incorrect_colour_datetype(self):
        engine = Engine2D()

        try:
            engine.change_colour(0)
        except AssertionError:
            pass
        else:
            raise AssertionError('No validation for invalid color data type')
