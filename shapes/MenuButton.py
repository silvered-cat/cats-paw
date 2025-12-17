from shapes.Button import Button
from pykraken import EventType, mouse, color, Color, Event, Rect, draw, Vec2


class MenuButton(Button):
    """A button used in menus that changes appearance when active."""

    INFLATION_AMOUNT = Vec2(20, 20)

    def __init__(self):
        super().__init__()
        self._isActive = False
        self._activeColor: Color = color.YELLOW
        self._normalColor: Color = self.getColor()

    def draw(self) -> None:
        super().draw()
        if self.isActive():
            draw.rect(self.getRect(), self._activeColor, self.getThickness())
        else:
            draw.rect(self.getRect(), self._normalColor, self.getThickness())

    def setActiveColor(self, activeColor: Color) -> MenuButton:
        """Sets the color to use when the button is active."""
        self._activeColor = activeColor
        return self

    def activate(self) -> MenuButton:
        """Active means the button is being hovered over."""
        if self.isActive():
            return self
        self.setActive(True)
        self.getRect().inflate(MenuButton.INFLATION_AMOUNT)
        return self

    def deactivate(self) -> MenuButton:
        """Deactivate means the button is no longer being hovered over."""
        if not self.isActive():
            return self
        self.setActive(False)
        self.getRect().inflate(-MenuButton.INFLATION_AMOUNT)
        return self

    def isActive(self) -> bool:
        """
        Returns whether the button is currently active (hovered over).
        This determines whether to draw the button with activeColor or normal color.
        """
        return self._isActive

    def setActive(self, isActive: bool) -> MenuButton:
        """Sets whether the button is currently active (hovered over)."""
        self._isActive = isActive
        return self

    def handleEvent(self, event: Event) -> None:
        """
        Handles mouse hover events to activate/deactivate the button.

        when the mouse moves, check if it's inside the button's rectangle and applies a size change accordingly.
        """
        if event.type == EventType.MOUSE_MOTION:
            mousePos = mouse.get_pos()
            x = mousePos.x
            y = mousePos.y
            rect = self.getRect()
            isInsideHorizontally = rect.left <= x and x <= rect.right
            isInsideVertically = rect.top <= y and y <= rect.bottom
            isInside = isInsideHorizontally and isInsideVertically

            if isInside and not self.isActive():
                self.activate()
            elif not isInside and self.isActive():
                self.deactivate()
