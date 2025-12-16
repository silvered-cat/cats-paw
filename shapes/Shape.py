import pykraken as kn
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for all shapes. Defines common properties and methods.
    Note: Remember to initialize pykraken before creating any shapes!

    Attributes:
        _position (kn.Vec2): The position of the shape.
        _color (kn.Color): The color of the shape.
    """

    def __init__(self) -> None:
        super().__init__()
        self._position = kn.Vec2(0, 0)
        self._color = kn.color.GREY

    @abstractmethod
    def setPosition(self, x: float, y: float) -> Shape:
        """
        Determines the position of the shape relative to the window.
        Note: (0,0) is the top-left corner of the window.
        Args:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
        """
        pass

    @abstractmethod
    def getPosition(self) -> kn.Vec2:
        """Returns the current position of the shape. Unless set, defaults to center of shape."""
        pass

    def setColor(self, color: kn.Color) -> Shape:
        """Sets the color of the shape unless a texture is applied."""
        self._color = color
        return self

    def getColor(self) -> kn.Color:
        """Returns the current color of the shape."""
        return self._color

    @abstractmethod
    def draw(self) -> None:
        """Wraps the drawing logic from pykraken."""
        pass
