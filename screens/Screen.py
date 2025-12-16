import abc
from queue import Queue
from shapes.Shape import Shape
from pykraken import Event


class Screen(abc.ABC):

    @abc.abstractmethod
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def run(self, renderQueue: Queue[Shape]) -> None:
        pass

    @abc.abstractmethod
    def handleEvent(self, event: Event) -> None:
        pass
