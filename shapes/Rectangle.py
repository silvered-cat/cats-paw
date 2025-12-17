from .Shape import Shape
import pykraken as kn
import typing

Texture = kn.Texture


class Rectangle(Shape):
    """
    Represents a rectangle shape that can be drawn on the screen. Inherits from Shape.
    Attributes:
        _rect (Rect): An instance of the pykraken Rect class.
        _texture (Texture | None): The texture applied to the rectangle, if any.
        _dimensions (Vec2): The width and height of the rectangle using the pykraken Vec2 class.
        _thickness (int): The thickness of the rectangle's border.

    """

    def __init__(self):
        super().__init__()
        self._rect = kn.Rect()
        rect = kn.Rect()
        self._rect: kn.Rect = rect
        self._thickness = 1

    def draw(self) -> None:
        color = self.getColor()
        rect = self.getRect()
        thick = self.getThickness()
        kn.draw.rect(rect, color, thick)

    def setThickness(self, thickness: int) -> Rectangle:
        self._thickness = thickness
        return self

    def getThickness(self) -> int:
        return self._thickness

    def getRect(self) -> kn.Rect:
        return self._rect

    def setRect(self, rect: kn.Rect) -> Rectangle:
        """Sets the internal Rect instance."""
        self._rect = rect
        return self

    def setDimensions(self, width: float, height: float) -> Rectangle:
        """Updates the dimensions of the rectangle."""
        self.getRect().w = width
        self.getRect().h = height
        return self

    def getDimensions(self) -> kn.Vec2:
        return self.getRect().size

    @typing.override
    def setPosition(self, x: float, y: float) -> Rectangle:
        """Sets the rectangle's coordinates relative to the window from the center of the shape. Note: (0,0) is the top left of the screen."""
        self._position = kn.Vec2(x, y)
        self.getRect().center = self._position
        return self

    @typing.override
    def setColor(self, color: kn.Color) -> Rectangle:
        super().setColor(color)
        return self

    @typing.override
    def getPosition(self) -> kn.Vec2:
        return self.getRect().center
