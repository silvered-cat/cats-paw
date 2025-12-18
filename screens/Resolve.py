from queue import Queue
from pykraken import Event

from shapes.Shape import Shape
from .Screen import Screen
from state.Game import Game


class Resolve(Screen):
    def __init__(self, game: Game):
        super().__init__(game)
        self._elements: list[Shape] = []
        self._eventElements: list[Shape] = []

    def handleEvent(self, event: Event) -> None:
        return super().handleEvent(event)

    def run(self, renderQueue: Queue[Shape]) -> None:
        return super().run(renderQueue)
