from shapes.ShapeFactory import ShapeFactory
from shapes.Shape import Shape
from .Screen import Screen
from queue import Queue


class Menu(Screen):

    def __init__(self, monitor_size: tuple[float, float]) -> None:
        super().__init__(monitor_size)
        self._shapes = ShapeFactory()
        self._options: tuple[Shape, Shape] = (
            self.makeStartButton(monitor_size),
            self.makeQuitButton(monitor_size),
        )

    def makeStartButton(self, monitor_size: tuple[float, float]):
        xOffset = monitor_size[0] / 5
        yOffset = monitor_size[1] / 2
        button = self._shapes.createTextBox("Start Game")
        button.setPosition(xOffset, yOffset).setDimensions(200, 50)
        return button

    def makeQuitButton(self, monitor_size: tuple[float, float]):
        xOffset = monitor_size[0] / 5
        xOffset = monitor_size[0] - xOffset
        yOffset = monitor_size[1] / 2
        button = self._shapes.createTextBox("Quit Game")
        button.setPosition(xOffset, yOffset).setDimensions(200, 50)
        return button

    def run(self, renderQueue: Queue[Shape]) -> None:
        renderQueue.put(self._options[0])
        renderQueue.put(self._options[1])
        return
