from state.State import State
from screens.screensEnum import ScreensEnum
import pykraken as kn


class Game(State):
    def __init__(self):
        self._playerScore = 0
        self._npcScore = 0
        self._current_screen: ScreensEnum
        initialScreen = ScreensEnum.MENU
        self.setCurrentScreen(initialScreen)

    def getWindowSize(self) -> tuple[float, float]:
        win = kn.window.get_size()
        return (win.x, win.y)

    def setCurrentScreen(self, screen: ScreensEnum) -> Game:
        self._current_screen = screen
        return self

    def getCurrentScreen(self) -> ScreensEnum:
        return self._current_screen
