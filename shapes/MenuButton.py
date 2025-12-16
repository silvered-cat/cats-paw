from shapes.Button import Button
from pykraken import Vec2, EventType, mouse, color, Color, Event


class MenuButton(Button):
    ACTIVE_SCALE = 1.1

    def __init__(self):
        super().__init__()
        self._normalDimensions = self.getDimensions().copy()
        self._isActive = False
        self._activeColor: Color = color.YELLOW
        self._normalColor: Color = self.getColor()

    def getNormalDimensions(self) -> Vec2:
        return self._normalDimensions

    def setNormalDimensions(self, dimensions: Vec2) -> MenuButton:
        self._normalDimensions = dimensions
        return self

    def setColor(self, color: Color) -> MenuButton:
        super().setColor(color)
        self._normalColor = color
        return self

    def setActiveColor(self, activeColor: Color) -> MenuButton:
        self._activeColor = activeColor
        return self

    def activate(self) -> MenuButton:
        print("Activating Button")
        if self.isActive():
            return self
        currentDimensions = self.getNormalDimensions().copy()
        currentDimensions.scale_to_length(MenuButton.ACTIVE_SCALE)
        currentDimensions.rotate(90)
        self.setDimensions(currentDimensions.x, currentDimensions.y)
        self.setColor(self._activeColor)
        self.setActive(True)
        self.draw()
        return self

    def deactivate(self) -> MenuButton:
        if not self.isActive():
            return self
        normalDimensions = self.getNormalDimensions()
        self.setDimensions(normalDimensions.x, normalDimensions.y)
        self.setActive(False)
        self.setColor(self._normalColor)
        self.draw()
        return self

    def isActive(self) -> bool:
        return self._isActive

    def setActive(self, isActive: bool) -> MenuButton:
        self._isActive = isActive
        return self

    def handleEvent(self, event: Event) -> None:

        if event.type == EventType.MOUSE_MOTION:
            thisButton = self.getRect()
            leftBound = thisButton.left
            rightBound = thisButton.right
            topBound = thisButton.bottom  # Found a bug here, was inverted
            bottomBound = thisButton.top  # Found a bug here, was inverted
            mousePos = mouse.get_pos()
            isInsideHorizontally = leftBound <= mousePos.x and mousePos.x <= rightBound
            isInsideVertically = bottomBound <= mousePos.y and mousePos.y <= topBound
            isInside = isInsideHorizontally and isInsideVertically
            print(
                f"mousePos.x: {mousePos.x}, mousePos.y: {mousePos.y}, Button Bounds: L:{leftBound}, R:{rightBound}, T:{topBound}, B:{bottomBound}"
            )
            if isInside:
                print("Running the Events in: MenuButton")
                self.activate()
            else:
                self.deactivate()
