import pykraken as kn
from screens.Screen import Screen
from screens.screensEnum import ScreensEnum
from queue import Queue
from shapes.Shape import Shape
from state.Game import Game
from shapes.ShapeFactory import ShapeFactory

sf = ShapeFactory()

# position constants
TOP_ROW_Y = 0.25
BOTTOM_ROW_Y = 0.66
INIT_ARROW_ROW_Y = 0.50

NPC_SCORE_POS = (0.15, TOP_ROW_Y)
PLAYER_SCORE_POS = (0.85, TOP_ROW_Y)
TIMER_POS = (0.50, TOP_ROW_Y)
NPC_CHOICE_POS = (0.15, BOTTOM_ROW_Y)

PLAYER_CHOICE_POS = (0.75, BOTTOM_ROW_Y)
LEFT_ARROW_POS = (0.70, INIT_ARROW_ROW_Y)
RIGHT_ARROW_POS = (0.90, INIT_ARROW_ROW_Y)

# size constants
INFO_BOX_SIZE = 0.10
PAW_BOX_SIZE = 0.20
CLICKABLE_SIZE = 0.05


class Battle(Screen):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self._game = game
        self._elements: list[Shape] = []
        self.makeElements()

    def handleEvent(self, event: kn.Event):
        # Handle events specific to the Battle screen
        pass

    def run(self, renderQueue: Queue[Shape]):
        # Update and render the Battle screen
        for element in self._elements:
            renderQueue.put(element)
        return

    def makeElements(self):
        self._elements.append(self.makeNPCScore())
        self._elements.append(self.makePlayerScore())
        self._elements.append(self.makeNPCChoice())
        self._elements.append(self.makeTimer())
        self._elements.append(self.makePlayerChoice())
        self._elements.append(self.makeLeftArrow())
        self._elements.append(self.makeRightArrow())

    def makeNPCScore(self) -> Shape:
        # Generate NPC score logic
        initWindowSize = self._game.getWindowSize()
        box = sf.createTextBox()
        (
            box.setContent("NPC Score\n0")
            .setPosition(
                initWindowSize[0] * NPC_SCORE_POS[0],
                initWindowSize[1] * NPC_SCORE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * INFO_BOX_SIZE, initWindowSize[1] * INFO_BOX_SIZE
            )
        )
        return box

    def makePlayerScore(self) -> Shape:
        # Generate Player score logic
        initWindowSize = self._game.getWindowSize()
        box = sf.createTextBox()
        (
            box.setContent("Player Score\n0")
            .setPosition(
                initWindowSize[0] * PLAYER_SCORE_POS[0],
                initWindowSize[1] * PLAYER_SCORE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * INFO_BOX_SIZE, initWindowSize[1] * INFO_BOX_SIZE
            )
        )
        return box

    def makeTimer(self) -> Shape:
        # Generate Timer logic
        initWindowSize = self._game.getWindowSize()
        box = sf.createTextBox()
        (
            box.setContent("Time\n5")
            .setPosition(
                initWindowSize[0] * TIMER_POS[0],
                initWindowSize[1] * TIMER_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * INFO_BOX_SIZE, initWindowSize[1] * INFO_BOX_SIZE
            )
        )
        return box

    def makeNPCChoice(self) -> Shape:
        # Generate NPC choice logic
        initWindowSize = self._game.getWindowSize()
        box = sf.createTextBox()
        (
            box.setContent("NPC Choice")
            .setPosition(
                initWindowSize[0] * NPC_CHOICE_POS[0],
                initWindowSize[1] * NPC_CHOICE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * PAW_BOX_SIZE, initWindowSize[1] * PAW_BOX_SIZE
            )
        )
        return box

    def makePlayerChoice(self) -> Shape:
        # Generate Player choice logic
        initWindowSize = self._game.getWindowSize()
        box = sf.createTextBox()
        (
            box.setContent("Player Choice")
            .setPosition(
                initWindowSize[0] * PLAYER_CHOICE_POS[0],
                initWindowSize[1] * PLAYER_CHOICE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * PAW_BOX_SIZE, initWindowSize[1] * PAW_BOX_SIZE
            )
        )
        return box

    def makeLeftArrow(self) -> Shape:
        # Generate Left Arrow logic
        initWindowSize = self._game.getWindowSize()
        box = sf.createTextBox()
        (
            box.setContent("<")
            .setPosition(
                initWindowSize[0] * LEFT_ARROW_POS[0],
                initWindowSize[1] * LEFT_ARROW_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * CLICKABLE_SIZE, initWindowSize[1] * CLICKABLE_SIZE
            )
        )
        return box

    def makeRightArrow(self) -> Shape:
        # Generate Right Arrow logic
        initWindowSize = self._game.getWindowSize()
        box = sf.createTextBox()
        (
            box.setContent(">")
            .setPosition(
                initWindowSize[0] * RIGHT_ARROW_POS[0],
                initWindowSize[1] * RIGHT_ARROW_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * CLICKABLE_SIZE, initWindowSize[1] * CLICKABLE_SIZE
            )
        )
        return box
