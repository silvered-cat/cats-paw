from queue import Queue
from pykraken import Event, EventType
from shapes.Shape import Shape
from .Screen import Screen
from shapes.UpdatingTextBox import UpdatingTextBox
from state.Game import Game
from utils.StatusEnums import StatusEnums
from .screensEnum import ScreensEnum
from shapes.ShapeFactory import sf
from utils.OutcomeCalculator import OutcomeCalculator
from utils.OutcomeEnum import OutcomeEnum
from utils.messageMarquee import MessageMarquee
from utils.Timer import Timer

# Constants
# UI element positions:
TOP_ROW_Y = 0.25
BOTTOM_ROW_Y = 0.66
HORIZONTAL_MIDDLE = 0.4

# Element specific x coords
NPC_LEFT = 0.25
PLAYER_RIGHT = 0.75

# Positions
TOP_CENTER_MESSAGE = (HORIZONTAL_MIDDLE, TOP_ROW_Y)
NPC = (NPC_LEFT, BOTTOM_ROW_Y)
PLAYER = (PLAYER_RIGHT, BOTTOM_ROW_Y)

# Sizes
MESSAGE_BOX = (0.20, 0.1, 32)  # L, W, and font size
CHARACTER_BOX = (0.2, 0.2)  # Only using one variable to make a box

# Messages
PRESS_ANY_KEY = "--Press any key to continue!--"
WIN = "Player Win!--"  # 11 chars + 2 space
DRAW = "Catnip!------"  # 7 chars + 6 spaces
LOSS = "Computer Win!  "  # 13 chars
MESSAGE_LENGTH = 13  # number of chars to display at a time.
RENDER_TIME = 0.125
RESET_TEXT_TIME_MARKER: None = None
INIT_TIMER = 5.00


class Resolve(Screen):
    def __init__(self, game: Game):
        super().__init__(game)
        self._elements: list[Shape] = []
        self._eventElements: list[Shape] = []
        self._game = game
        self._outcomeMessage: str
        self._outcome: None | OutcomeEnum = None
        self._messageBox: UpdatingTextBox
        self._textTime: None | Timer = RESET_TEXT_TIME_MARKER
        self._marquee: None | MessageMarquee = None
        self._textRenderTime: float = RENDER_TIME
        self._substring = ""
        self._makeElements()

    def handleEvent(self, event: Event) -> None:
        super().handleEvent(event)
        for el in self._elements:
            el.handleEvent(event)
        self._awaitPlayerResponse(event)

    def run(self, renderQueue: Queue[Shape]) -> None:
        # Needs to calculate the results and render them
        if self._game.getRoundStatus() is StatusEnums.END:
            self._calculateAndSetResults()

        for el in self._elements:
            renderQueue.put(el)

    # Should handle setting the correct outcome of the round.
    def _calculateAndSetResults(self):
        if self._outcome is not None:
            return
        outcome = OutcomeCalculator.determineOutcome(
            self._game.getPlayerChoice(), self._game.getOpponentChoice()
        )
        self._outcome = outcome
        if outcome is OutcomeEnum.DRAW:
            self._outcomeMessage = DRAW
        elif outcome is OutcomeEnum.WIN:
            self._outcomeMessage = WIN
            self._game.incrementPlayerScore()
        elif outcome is OutcomeEnum.LOSE:
            self._outcomeMessage = LOSS
            self._game.incrementNPCScore()

        self._marquee = MessageMarquee(self._outcomeMessage + PRESS_ANY_KEY)
        self._substring = self._makeMessageText()
        self._setFirstTimer()

    def _setFirstTimer(self):
        self._textTime = Timer()
        self._textTime.setTimer(INIT_TIMER)
        self._textTime.start()

    def _setTimer(self):
        self._textTime = Timer()
        self._textTime.setTimer(RENDER_TIME)
        self._textTime.start()

    def _makeMessageText(self) -> str:
        if self._marquee is None:
            raise TypeError("Expected an instance of Message Marquee but found None.")

        strBuilder = ""
        strBuilder = self._substring
        if len(strBuilder) < MESSAGE_LENGTH:
            while len(strBuilder) < MESSAGE_LENGTH:
                strBuilder += self._marquee.getChar()
            return strBuilder
        strBuilder = strBuilder[1:] + self._marquee.getChar()
        return strBuilder

    # Should decide what the next screen should be based on results and game state while cleaning state.
    def _setNextScreenAndCleanup(self):
        self._game.setCurrentScreen(ScreensEnum.BATTLE)
        self._game.setRoundStatus(StatusEnums.START)
        self._outcome = None
        self._textTime = None
        self._marquee = None
        self._substring = ""

    # This is the "press any key to continue thing."
    def _awaitPlayerResponse(self, event: Event):

        if event.type == EventType.KEY_DOWN:
            self._setNextScreenAndCleanup()

    def _makeElements(self):
        self._messageBox = self._makeTopMessage()
        self._elements.append(self._messageBox)
        self._elements.append(self._makeNPC())
        self._elements.append(self._makePlayer())

    def _makeTopMessage(self) -> UpdatingTextBox:
        textBox = sf.createUpdatingTextBox()
        window = self._game.getWindowSize()
        dimensions = (window[0] * MESSAGE_BOX[0], window[1] * MESSAGE_BOX[1])
        (
            textBox.setUpdateFunction(self.updateMessageBox)
            .setFontSize(MESSAGE_BOX[2])
            .setContent("Who won?")
            .setPosition(
                window[0] * TOP_CENTER_MESSAGE[0], window[1] * TOP_CENTER_MESSAGE[1]
            )
            .setDimensions(dimensions[0], dimensions[1])
        )
        return textBox

    def updateMessageBox(self) -> str:
        if self._textTime is None:
            return "Oops!"

        if self._textTime.isFinished():
            self._setTimer()
            self._substring = self._makeMessageText()
        return self._substring

    def _makeNPC(self) -> Shape:
        box = sf.createRectangle()
        window = self._game.getWindowSize()
        dimensions = (CHARACTER_BOX[0] * window[0], CHARACTER_BOX[1] * window[1])

        (
            box.setPosition(window[0] * NPC[0], window[1] * NPC[1]).setDimensions(
                dimensions[0], dimensions[1]
            )
        )
        return box

    def _makePlayer(self) -> Shape:
        box = sf.createRectangle()
        window = self._game.getWindowSize()
        dimensions = (CHARACTER_BOX[0] * window[0], CHARACTER_BOX[1] * window[1])

        (
            box.setPosition(window[0] * PLAYER[0], window[1] * PLAYER[1]).setDimensions(
                dimensions[0], dimensions[1]
            )
        )
        return box
