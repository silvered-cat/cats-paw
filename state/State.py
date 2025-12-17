import abc
from screens.screensEnum import ScreensEnum


class State(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def getWindowSize(self) -> tuple[float, float]:
        pass

    @abc.abstractmethod
    def setCurrentScreen(self, screen: ScreensEnum) -> State:
        pass

    @abc.abstractmethod
    def getCurrentScreen(self) -> ScreensEnum:
        pass
