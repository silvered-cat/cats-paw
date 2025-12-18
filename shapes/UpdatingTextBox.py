from .TextBox import TextBox
from typing import Callable


class UpdatingTextBox(TextBox):
    def __init__(self):
        self._updateFunction: Callable[[], str] = lambda: "I'm empty!"
        super().__init__()

    def setUpdateFunction(self, updateFunc: Callable[[], str]) -> UpdatingTextBox:
        """Binds a function that returns a string to be called every frame to update the content of the TextBox."""
        self._updateFunction = updateFunc
        return self

    def getUpdateFunction(self) -> Callable[[], str]:
        """Returns the function bound to update the content of the TextBox."""
        return self._updateFunction

    def draw(self):
        """Updates the content by calling the bound function and then draws the TextBox."""
        newContent = self.getUpdateFunction()()
        self.setContent(newContent)
        super().draw()
