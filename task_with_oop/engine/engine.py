from typing import List
from task_with_oop.shapes.base import BaseShape


class Engine2D:
    _canvas = []
    _colour = None

    def add_shapes_to_canvas(self, shapes: List[BaseShape]):
        for shape in shapes:
            assert isinstance(shape, BaseShape), 'Another data type was passed, shape expected'
            self._canvas.append(shape)

    def draw(self):
        assert self._canvas, 'There are no shapes to draw'

        for shape in self._canvas:
            shape.draw(self._colour)

        self._canvas.clear()

    def change_colour(self, colour: str):
        assert type(colour) == str, 'Another data type was passed, string expected'
        self._colour = colour
