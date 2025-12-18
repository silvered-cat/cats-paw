from shapes.ShapeFactory import ShapeFactory
from shapes.Shape import Shape
from shapes.MenuButton import MenuButton
from .Screen import Screen
from queue import Queue
from pykraken import color, Event, window
from state.Game import Game
from screens.screensEnum import ScreensEnum


class Menu(Screen):
    """
    Menu Screen Class. Handles rendering and events for the main menu.

    Attributes:
        BUTTON_RATIO (float) STATIC : Ratio of button size to screen size.
        _shapes (ShapeFactory): Factory for creating shapes.
        _options (tuple[MenuButton, MenuButton]): Tuple containing the Start and Quit buttons
        _game (Game): Reference to the game state.

    Note: Does not handle screen resizing events.
    """

    BUTTON_RATIO = 0.1

    def __init__(self, gameState: Game) -> None:
        super().__init__(gameState)
        self._shapes = ShapeFactory()
        options: list[Shape] = [
            self.makeStartButton(gameState.getWindowSize()),
            self.makeQuitButton(gameState.getWindowSize()),
        ]
        self._options: list[Shape] = options
        self._game = gameState

    def makeStartButton(self, monitor_size: tuple[float, float]) -> MenuButton:
        """Creates the start button for the menu screen."""

        w = monitor_size[0] * self.BUTTON_RATIO
        h = monitor_size[1] * self.BUTTON_RATIO

        x = monitor_size[0] / 4
        y = monitor_size[1] * 0.75

        button = self._shapes.createMenuButton()
        (
            button.setActiveColor(color.GREEN)
            .setCallback(self.startCallback)
            .setTextColor(color.WHITE)
            .setContent("Start Game")
            .setPosition(x, y)
            .setDimensions(w, h)
        )
        return button

    def startCallback(self) -> None:
        """Callback function for starting the game."""
        self._game.setCurrentScreen(ScreensEnum.BATTLE)

    def makeQuitButton(self, monitor_size: tuple[float, float]) -> MenuButton:
        """Creates the quit button for the menu screen."""

        w = monitor_size[0] * self.BUTTON_RATIO
        h = monitor_size[1] * self.BUTTON_RATIO

        x = monitor_size[0] * 0.75
        y = monitor_size[1] * 0.75

        button = self._shapes.createMenuButton()
        (
            button.setActiveColor(color.GREEN)
            .setCallback(self.quitCallback)
            .setTextColor(color.WHITE)
            .setContent("Quit Game")
            .setPosition(x, y)
            .setDimensions(w, h)
        )
        return button

    def quitCallback(self) -> None:
        """Callback function for quitting the game."""
        window.close()

    def run(self, renderQueue: Queue[Shape]) -> None:
        """Handles the rendering order of the menu screen."""
        renderQueue.put(self._options[0])
        renderQueue.put(self._options[1])
        return

    def getOptions(self) -> list[Shape]:
        """Returns the menu options (buttons)."""
        return self._options

    def handleEvent(self, event: Event) -> None:
        """Passes the event to each menu option for handling."""
        for option in self.getOptions():
            option.handleEvent(event)
