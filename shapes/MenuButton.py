from shapes.Button import Button
from pykraken import Vec2, EventType, mouse, color, Color


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
        currentDimensions = self.getNormalDimensions().copy()
        currentDimensions.scale_to_length(MenuButton.ACTIVE_SCALE)
        self.setDimensions(currentDimensions.x, currentDimensions.y)
        self.setColor(self._activeColor)
        self.setActive(True)
        return self

    def deactivate(self) -> MenuButton:
        normalDimensions = self.getNormalDimensions()
        self.setDimensions(normalDimensions.x, normalDimensions.y)
        self.setActive(False)
        self.setColor(self._normalColor)
        return self

    def isActive(self) -> bool:
        return self._isActive

    def setActive(self, isActive: bool) -> MenuButton:
        self._isActive = isActive
        return self

    def handleEvent(self, event: EventType) -> None:
        if event == EventType.MOUSE_MOTION:
            thisButton = self.getRect()
            leftBound = thisButton.left
            rightBound = thisButton.right
            topBound = thisButton.top
            bottomBound = thisButton.bottom
            mousePos = mouse.get_pos()
            isInsideHorizontally = (
                leftBound <= mousePos[0] and rightBound >= mousePos[0]
            )
            isInsideVertically = bottomBound <= mousePos[1] and topBound >= mousePos[1]
            isInside = isInsideHorizontally and isInsideVertically
            if isInside:
                self.activate()
            else:
                self.deactivate()
