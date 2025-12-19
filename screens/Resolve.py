from queue import Queue
from pykraken import Event

from shapes.Shape import Shape
from .Screen import Screen
from state.Game import Game
from utils.StatusEnums import StatusEnums
from .screensEnum import ScreensEnum


class Resolve(Screen):
    def __init__(self, game: Game):
        super().__init__(game)
        self._elements: list[Shape] = []
        self._eventElements: list[Shape] = []
        self._game = game

    def handleEvent(self, event: Event) -> None:
        return super().handleEvent(event)

    def run(self, renderQueue: Queue[Shape]) -> None:
        super().run(renderQueue)

        if self._game.getRoundStatus() is StatusEnums.END:
            pass
        elif self._game.getRoundStatus() is StatusEnums.START:
            self._game.setCurrentScreen(ScreensEnum.BATTLE)
