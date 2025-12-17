from shapes.Button import Button
from pykraken import EventType, mouse, color, Color, Event, Rect, draw, Vec2


class MenuButton(Button):
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

    def getOriginalSelf(self) -> Rect:
        return self._originalSelf

    def setOriginalSelf(self, rect: Rect) -> MenuButton:
        self._originalSelf = rect
        return self

    def setColor(self, color: Color) -> MenuButton:
        super().setColor(color)
        self._normalColor = color
        return self

    def setActiveColor(self, activeColor: Color) -> MenuButton:
        self._activeColor = activeColor
        return self

    def activate(self) -> MenuButton:
        if self.isActive():
            return self
        self.setActive(True)
        self.getRect().inflate(MenuButton.INFLATION_AMOUNT)
        return self

    def deactivate(self) -> MenuButton:
        if not self.isActive():
            return self
        self.setActive(False)
        self.getRect().inflate(-MenuButton.INFLATION_AMOUNT)
        return self

    def isActive(self) -> bool:
        return self._isActive

    def setActive(self, isActive: bool) -> MenuButton:
        self._isActive = isActive
        return self

    def handleEvent(self, event: Event) -> None:
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
