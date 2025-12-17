from shapes.ShapeFactory import ShapeFactory
from shapes.Shape import Shape
from shapes.MenuButton import MenuButton
from .Screen import Screen
from queue import Queue
from pykraken import color, Event
from state.Game import Game


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
        self._options: tuple[MenuButton, MenuButton] = (
            self.makeStartButton(gameState.getWindowSize()),
            self.makeQuitButton(gameState.getWindowSize()),
        )
        self._game = gameState

    def makeStartButton(self, monitor_size: tuple[float, float]) -> MenuButton:
        """Creates the start button for the menu screen."""
        dimensions = (
            monitor_size[0] * self.BUTTON_RATIO,
            monitor_size[1] * self.BUTTON_RATIO,
        )
        pos = (
            monitor_size[0] / 4,
            monitor_size[1] * 0.75,
        )
        button = self._shapes.createMenuButton(
            content="Start Game",
            position=pos,
            dimensions=dimensions,
            activeColor=color.GREEN,
            color=color.RED,
        )
        button.setTextColor(color.WHITE)
        return button

    def makeQuitButton(self, monitor_size: tuple[float, float]) -> MenuButton:
        """Creates the quit button for the menu screen."""
        dimensions = (
            monitor_size[0] * self.BUTTON_RATIO,
            monitor_size[1] * self.BUTTON_RATIO,
        )
        pos = (
            monitor_size[0] * 0.75,
            monitor_size[1] * 0.75,
        )
        button = self._shapes.createMenuButton(
            content="Quit Game",
            position=pos,
            dimensions=dimensions,
            activeColor=color.GREEN,
            color=color.GREY,
        )
        button.setTextColor(color.WHITE)
        return button

    def run(self, renderQueue: Queue[Shape]) -> None:
        """Handles the rendering order of the menu screen."""
        renderQueue.put(self._options[0])
        renderQueue.put(self._options[1])
        return

    def getOptions(self) -> tuple[MenuButton, MenuButton]:
        """Returns the menu options (buttons)."""
        return self._options

    def handleEvent(self, event: Event) -> None:
        """Passes the event to each menu option for handling."""
        for option in self.getOptions():
            option.handleEvent(event)
