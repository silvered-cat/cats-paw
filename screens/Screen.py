import abc
from queue import Queue
from shapes.Shape import Shape


class Screen(abc.ABC):
    @abc.abstractmethod
    def __init__(self, monitor_size: tuple[float, float]) -> None:
        self._monitor_size = monitor_size

    @abc.abstractmethod
    def run(self, renderQueue: Queue[Shape]) -> None:
        pass
