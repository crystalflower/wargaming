from abc import ABC, abstractmethod


class BaseShape(ABC):
    def __init__(
            self,
            first_x: int,
            first_y: int
    ):
        self.first_x = first_x
        self.first_y = first_y

    @abstractmethod
    def draw(self):
        pass
