import abc
from queue import Queue
from shapes.Shape import Shape


class Screen(abc.ABC):

    @abc.abstractmethod
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def run(self, renderQueue: Queue[Shape]) -> None:
        pass
