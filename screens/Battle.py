import pykraken as kn
from screens.Screen import Screen
from screens.screensEnum import ScreensEnum
from queue import Queue
from shapes.Shape import Shape
from state.Game import Game
from shapes.ShapeFactory import sf
from shapes.UpdatingTextBox import UpdatingTextBox
from utils.ChoiceEnum import ChoiceEnum
from utils.ChoiceCarousel import ChoiceCarousel
from utils.choiceStringMapper import getChoiceString
from utils.StatusEnums import StatusEnums
from shapes.MenuButton import MenuButton

# position constants are multipliers of window size. Ex: (0.5, 0.5) is center of screen
TOP_ROW_Y = 0.25
BOTTOM_ROW_Y = 0.66
INIT_ARROW_ROW_Y = 0.50
# These positions should not change after the game starts.
NPC_SCORE_POS = (0.15, TOP_ROW_Y)
PLAYER_SCORE_POS = (0.85, TOP_ROW_Y)
TIMER_POS = (0.50, TOP_ROW_Y)
NPC_CHOICE_POS = (0.15, BOTTOM_ROW_Y)
PLAYER_CHOICE_POS = (0.75, BOTTOM_ROW_Y)
# These positions WILL change during the game.
LEFT_ARROW_POS = (0.70, INIT_ARROW_ROW_Y)
RIGHT_ARROW_POS = (0.90, INIT_ARROW_ROW_Y)

# size constants that will scale with window size. Ex: 0.1 is 10% of window size
INFO_BOX_SIZE = 0.10
PAW_BOX_SIZE = 0.20
CLICKABLE_SIZE = 0.05

# Game constants
ROUND_TIME_LIMIT_SECONDS = 20.00


class Battle(Screen):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

        # init the attributes.
        self._game = game
        self._elements: list[Shape] = []
        self._NPCCarousel = ChoiceCarousel()
        self._playerCarousel = ChoiceCarousel()
        self.makeElements()
        game.setRoundTimeLimit(ROUND_TIME_LIMIT_SECONDS)
        game.resetScores()

    def handleEvent(self, event: kn.Event):
        """Passes events to the Battle screen elements to handle."""
        for el in self._elements:
            el.handleEvent(event)

    def run(self, renderQueue: Queue[Shape]):
        """Runs the Battle screen logic and queues elements for rendering."""
        if self._game.getRoundStatus() is StatusEnums.START:
            self._game.setRoundTimeLimit(ROUND_TIME_LIMIT_SECONDS)
            self._game.startCountdownTimer()
            self._game.setRoundStatus(StatusEnums.IN_PROGRESS)
        elif self._game.getRoundStatus() is StatusEnums.IN_PROGRESS:

            if self._game.isTimeUp():
                self._game.setOpponentChoice(self._NPCCarousel.getCurrentChoice())
                self._game.setPlayerChoice(self._playerCarousel.getCurrentChoice())
                self._game.setRoundStatus(StatusEnums.END)
            for element in self._elements:
                renderQueue.put(element)
        elif self._game.getRoundStatus() is StatusEnums.END:
            self._game.setCurrentScreen(ScreensEnum.RESOLVE)

        return

    def makeElements(self):
        """Creates all the starting elements on screen."""
        self._elements.append(self.makeNPCScore())
        self._elements.append(self.makePlayerScore())
        self._elements.append(self.makeNPCChoice())
        self._elements.append(self.makeTimer())
        self._elements.append(self.makePlayerChoice())
        self._elements.append(self.makeLeftArrow())
        self._elements.append(self.makeRightArrow())

    def makeNPCScore(self) -> Shape:
        """Makes the NPC score display."""
        initWindowSize = self._game.getWindowSize()
        box: UpdatingTextBox = sf.createUpdatingTextBox()

        (
            box.setUpdateFunction(self.updateNPCScoreBox)
            .setContent("NPC Score\n0")
            .setPosition(
                initWindowSize[0] * NPC_SCORE_POS[0],
                initWindowSize[1] * NPC_SCORE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * INFO_BOX_SIZE, initWindowSize[1] * INFO_BOX_SIZE
            )
        )

        return box

    def updateNPCScoreBox(self) -> str:
        formattedScore = f"NPC Score\n{self._game.getNPCScore()}"
        return formattedScore

    def testGameUpdate(self):
        """Testing method. For dev purposes only."""
        self._game.incrementNPCScore()
        self._game.incrementPlayerScore()

    def makePlayerScore(self) -> Shape:
        """Makes the player score UI element."""
        initWindowSize = self._game.getWindowSize()
        box = sf.createUpdatingTextBox()
        (
            box.setUpdateFunction(self.updatePlayerScoreBox)
            .setContent("Player Score\n0")
            .setPosition(
                initWindowSize[0] * PLAYER_SCORE_POS[0],
                initWindowSize[1] * PLAYER_SCORE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * INFO_BOX_SIZE, initWindowSize[1] * INFO_BOX_SIZE
            )
        )
        return box

    def updatePlayerScoreBox(self) -> str:
        """Internal method consumed by the player score UI element."""
        formattedScore = f"Player Score\n{self._game.getPlayerScore()}"
        return formattedScore

    def makeTimer(self) -> Shape:
        """Makes the timer UI element."""
        initWindowSize = self._game.getWindowSize()
        box = sf.createUpdatingTextBox()
        (
            box.setUpdateFunction(self.updateTimerBox)
            .setContent("Time\n5")
            .setPosition(
                initWindowSize[0] * TIMER_POS[0],
                initWindowSize[1] * TIMER_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * INFO_BOX_SIZE, initWindowSize[1] * INFO_BOX_SIZE
            )
        )
        return box

    def updateTimerBox(self) -> str:
        """Method intended to be consumed by UpdatingTextBox's update method."""
        remainingTime = self._game.getRemainingTime()
        formattedTime = f"Time\n{remainingTime:.2f}"
        return formattedTime

    def makeNPCChoice(self) -> Shape:
        """Generates the NPC choice UI element."""
        initWindowSize = self._game.getWindowSize()
        box = sf.createUpdatingTextBox()
        (
            box.setUpdateFunction(self.updateNPCChoice)
            .setContent("NPC Choice")
            .setPosition(
                initWindowSize[0] * NPC_CHOICE_POS[0],
                initWindowSize[1] * NPC_CHOICE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * PAW_BOX_SIZE, initWindowSize[1] * PAW_BOX_SIZE
            )
        )
        return box

    def updateNPCChoice(self) -> str:
        """Internal method that is consumed by the NPC choice UI element."""

        choice: ChoiceEnum = self._NPCCarousel.getCurrentChoice()

        choiceEnum = choice
        choiceStr = getChoiceString(choiceEnum)

        return choiceStr

    def makePlayerChoice(self) -> Shape:
        """Generates the  choice UI element."""
        initWindowSize = self._game.getWindowSize()
        box = sf.createUpdatingTextBox()
        (
            box.setUpdateFunction(self.updatePlayerChoice)
            .setContent("Player Choice")
            .setPosition(
                initWindowSize[0] * PLAYER_CHOICE_POS[0],
                initWindowSize[1] * PLAYER_CHOICE_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * PAW_BOX_SIZE, initWindowSize[1] * PAW_BOX_SIZE
            )
        )
        return box

    def updatePlayerChoice(self) -> str:
        """Internal method that is consumed by the Player choice UI element."""

        choice: ChoiceEnum = self._playerCarousel.getCurrentChoice()

        choiceEnum = choice
        choiceStr = getChoiceString(choiceEnum)

        return choiceStr

    def makeLeftArrow(self) -> MenuButton:
        """This UI element is responsible for dictating what goes on the user choice UI element in reverse."""
        initWindowSize = self._game.getWindowSize()
        box = sf.createMenuButton()
        (
            box.setActiveColor(kn.color.GREEN)
            .setCallback(self.onClickLeft)
            .setContent("<")
            .setPosition(
                initWindowSize[0] * LEFT_ARROW_POS[0],
                initWindowSize[1] * LEFT_ARROW_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * CLICKABLE_SIZE, initWindowSize[1] * CLICKABLE_SIZE
            )
        )
        return box

    def onClickLeft(self):
        """Internal method to be consumed by the onClick method in a Button class. Advances the internal player carousel to the left."""
        self._playerCarousel.previousNode()

    def makeRightArrow(self) -> MenuButton:
        """This UI element is responsible for dictating what goes on the user choice UI element next."""
        initWindowSize = self._game.getWindowSize()
        box = sf.createMenuButton()
        (
            box.setActiveColor(kn.color.GREEN)
            .setCallback(self.onClickRight)
            .setContent(">")
            .setPosition(
                initWindowSize[0] * RIGHT_ARROW_POS[0],
                initWindowSize[1] * RIGHT_ARROW_POS[1],
            )
            .setDimensions(
                initWindowSize[0] * CLICKABLE_SIZE, initWindowSize[1] * CLICKABLE_SIZE
            )
        )
        return box

    def onClickRight(self):
        """Internal method to be consumed by the onClick method in a Button class. Advances the internal player carousel to the right."""
        self._playerCarousel.nextNode()
