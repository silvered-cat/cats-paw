from shapes.ShapeFactory import ShapeFactory
from shapes.Shape import Shape
from shapes.MenuButton import MenuButton
from .Screen import Screen
from queue import Queue
from pykraken import color, Event
from state.Game import Game


class Menu(Screen):
    BUTTON_RATIO = 0.1

    def __init__(self, gameState: Game) -> None:
        super().__init__()
        self._shapes = ShapeFactory()
        self._options: tuple[MenuButton, MenuButton] = (
            self.makeStartButton(gameState.getWindowSize()),
            self.makeQuitButton(gameState.getWindowSize()),
        )
        self._game = gameState

    def makeStartButton(self, monitor_size: tuple[float, float]) -> MenuButton:
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
        renderQueue.put(self._options[0])
        renderQueue.put(self._options[1])
        return

    def getOptions(self) -> tuple[MenuButton, MenuButton]:
        return self._options

    def handleEvent(self, event: Event) -> None:
        for option in self.getOptions():
            option.handleEvent(event)
