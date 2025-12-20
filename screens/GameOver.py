from queue import Queue
from pykraken import Event
from shapes.Shape import Shape
from state.Game import Game
from .Screen import Screen
from shapes.ShapeFactory import sf
from utils.Timer import Timer
from utils.asciiArt import ASCII_CAT_LOSS

# Constants

# Positional Constants
HORIZONTAL_X = 0.5
TOP_ROW_Y = 0.33
BOTTOM_ROW_Y = 0.66

MESSAGE_POS = (HORIZONTAL_X, TOP_ROW_Y)
PLAYER_POS = (HORIZONTAL_X, BOTTOM_ROW_Y)

# Size Constants
MESSAGE_DIM = (0.4, 0.2)
PLAYER_DIM = (0.2, 0.4)

FONT_SIZE = 32  # size is in pixels.

# Message
MESSAGE_BLINK_TIMER = 3
MESSAGE_CONTENT = (
    "     Game Over!     ",
    "You lost the game...",
    "   Press any Key.   ",
)


# Player

ASCII_CAT_FONT_SIZE = 25
CAT_TIMER = 2


class GameOver(Screen):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self._elements: list[Shape] = []
        self._game = game
        self._currentIndex = 0
        self._blinkTimer = MESSAGE_BLINK_TIMER
        self._timer: None | Timer = None
        self._message = MESSAGE_CONTENT
        self._catIndex = 0
        self._catTimer = Timer()
        self._catTimer.setTimer(CAT_TIMER)

        self._makeElements()

    def run(self, renderQueue: Queue[Shape]) -> None:

        for el in self._elements:
            renderQueue.put(el)

    def handleEvent(self, event: Event) -> None:

        for el in self._elements:
            el.handleEvent(event)

    def _makeElements(self):
        self._elements.append(self._makeGameOverMessage())
        self._elements.append(self._makePlayer())

    def _makeGameOverMessage(self) -> Shape:
        box = sf.createUpdatingTextBox()
        win = (self._game.getWindowSize()[0], self._game.getWindowSize()[1])
        dim = (win[0] * MESSAGE_DIM[0], win[1] * MESSAGE_DIM[1])
        pos = (win[0] * MESSAGE_POS[0], win[1] * MESSAGE_POS[1])
        (
            box.setUpdateFunction(self.messageBlink)
            .setContent(MESSAGE_CONTENT[0])
            .setDimensions(dim[0], dim[1])
            .setPosition(pos[0], pos[1])
        )

        return box

    def _makePlayer(self) -> Shape:
        win = (self._game.getWindowSize()[0], self._game.getWindowSize()[1])
        dim = (win[0] * PLAYER_DIM[0], win[1] * PLAYER_DIM[1])
        pos = (win[0] * PLAYER_POS[0], win[1] * PLAYER_POS[1])
        box = sf.createUpdatingTextBox()
        (
            box.setUpdateFunction(self._updateCat)
            .setContent(ASCII_CAT_LOSS[0])
            .setFontSize(ASCII_CAT_FONT_SIZE)
            .setDimensions(dim[0], dim[1])
            .setPosition(pos[0], pos[1])
        )
        return box

    def _updateCat(self) -> str:

        if self._catTimer.isFinished():
            self._catIndex += 1
            self._catIndex = self._catIndex % len(ASCII_CAT_LOSS)
            self._catTimer.restart()
            self._catTimer.start()

        return ASCII_CAT_LOSS[self._catIndex]

    def messageBlink(self) -> str:
        if self._timer is None:
            self._timer = Timer()
            self._timer.setTimer(self._blinkTimer)
            self._timer.start()

        if self._timer.isFinished():
            self._currentIndex += 1
            self._currentIndex = self._currentIndex % 3
            self._timer.restart()
            self._timer.start()
        return self._message[self._currentIndex]
