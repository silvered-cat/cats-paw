from .TextBox import TextBox
from typing import Callable


class Button(TextBox):
    def __init__(self):
        super().__init__()
        self._callback: Callable[[], None] = lambda: None

    def setCallback(self, callback: Callable[[], None]) -> Button:
        self._callback = callback
        return self

    def onClick(self) -> None:
        self._callback()
