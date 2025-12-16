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
        self._texture: Texture | None = None
        self._dimensions = kn.Vec2(100, 100)
        self._rect: kn.Rect = kn.Rect()
        self._thickness = 1
        self._updateRect()

    def draw(self) -> None:
        textures = self.getTexture()
        color = self.getColor()
        rect = self.getRect()
        thick = self.getThickness()

        if textures is not None:
            kn.renderer.draw(textures, rect)
        else:
            kn.draw.rect(rect, color, thick)

    def setThickness(self, thickness: int) -> Rectangle:
        self._thickness = thickness
        return self

    def getThickness(self) -> int:
        return self._thickness

    def _updateRect(self) -> None:
        """Internal method to update a wrapped Rect instance."""
        self._rect.center = self.getPosition()
        self._rect.w = self.getDimensions()[0]
        self._rect.h = self.getDimensions()[1]

    def getRect(self) -> kn.Rect:
        return self._rect

    def setTexture(self, texture: Texture) -> Rectangle:
        """Applies a texture to the rectangle."""
        self._texture = texture
        return self

    def getTexture(self) -> Texture | None:
        return self._texture

    def setDimensions(self, width: float, height: float) -> Rectangle:
        """Updates the dimensions of the rectangle."""
        self._dimensions = kn.Vec2(width, height)
        self._updateRect()
        return self

    def getDimensions(self) -> kn.Vec2:
        return self._dimensions

    @typing.override
    def setPosition(self, x: float, y: float) -> Rectangle:
        """Sets the rectangle's coordinates relative to the window from the center of the shape. Note: (0,0) is the top left of the screen."""
        self._position = kn.Vec2(x, y)
        self._updateRect()
        return self

    @typing.override
    def setColor(self, color: kn.Color) -> Rectangle:
        super().setColor(color)
        return self

    @typing.override
    def getPosition(self) -> kn.Vec2:
        return self._position
