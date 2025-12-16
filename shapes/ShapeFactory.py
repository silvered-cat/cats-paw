from .Rectangle import Rectangle
from .TextBox import TextBox
import pykraken as kn


class ShapeFactory:
    """Creates various Shape instances."""

    def __init__(self) -> None:
        pass

    def createRectangle(
        self,
        dimensions: tuple[float, float] = (100, 100),
        position: tuple[float, float] = (0, 0),
        color: kn.Color = kn.color.GRAY,
    ) -> Rectangle:
        """Creates a Rectangle shape with optional dimensions, position, and color."""
        rect = Rectangle()
        rect.setDimensions(dimensions[0], dimensions[1]).setPosition(
            position[0], position[1]
        ).setColor(color)
        return rect

    def createTextBox(
        self,
        content: str = "Meow!",
        fontSize: int = 24,
        dimensions: tuple[float, float] = (100, 100),
        position: tuple[float, float] = (0, 0),
        color: kn.Color = kn.color.GRAY,
    ) -> TextBox:
        """
        Creates a TextBox shape with optional content, font size, dimensions, position, and color.
        Note: TextBox uses kraken-clean font and size 24 by default. To change font size, use setFontSize() on the returned TextBox.
        """
        rect = TextBox()
        rect.setContent(content).setFontSize(fontSize).setDimensions(
            dimensions[0], dimensions[1]
        ).setPosition(position[0], position[1]).setColor(color)
        return TextBox()
