import pykraken as kn
from Screen import Screen
from screensEnum import ScreensEnum
from queue import Queue
from shapes.Shape import Shape
from state.Game import Game


class Battle(Screen):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self._game = game
        # Initialize Battle screen specific attributes here

    def handleEvent(self, event: kn.Event):
        # Handle events specific to the Battle screen
        pass

    def run(self, renderQueue: Queue[Shape]):
        # Update and render the Battle screen
        pass
