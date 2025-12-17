import abc
from queue import Queue
from shapes.Shape import Shape
from pykraken import Event
from state.Game import Game


class Screen(abc.ABC):
    """
    Abstract Base Class for different screens in the game.
    Each screen must implement methods to run its logic and handle events.
    Allows for easier consumption and management of different screens.
    """

    @abc.abstractmethod
    def __init__(self, game: Game) -> None:
        pass

    @abc.abstractmethod
    def run(self, renderQueue: Queue[Shape]) -> None:
        """ "Handles the rendering and logic for the screen."""
        pass

    @abc.abstractmethod
    def handleEvent(self, event: Event) -> None:
        """Handles an event for the screen."""
        pass
