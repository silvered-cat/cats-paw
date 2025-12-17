from .Rectangle import Rectangle
from .TextBox import TextBox
import pykraken as kn
from .MenuButton import MenuButton


# Default parameters
DEFAULT_COLOR = kn.color.GRAY
DEFAULT_DIMENSIONS = (100.00, 100.00)
DEFAULT_POSITION = (0.00, 0.00)
DEFAULT_CONTENT = "Meow!"
DEFAULT_FONT_SIZE = 24
DEFAULT_ACTIVE_COLOR = kn.color.YELLOW


class ShapeFactory:
    """Creates various Shape instances."""

    def __init__(self) -> None:
        pass

    def createRectangle(
        self,
        dimensions: tuple[float, float] = DEFAULT_DIMENSIONS,
        position: tuple[float, float] = DEFAULT_POSITION,
        color: kn.Color = DEFAULT_COLOR,
    ) -> Rectangle:
        """Creates a Rectangle shape with optional dimensions, position, and color."""
        rect = Rectangle()
        rect.setDimensions(dimensions[0], dimensions[1]).setPosition(
            position[0], position[1]
        ).setColor(color)
        return rect

    def createTextBox(
        self,
        content: str = DEFAULT_CONTENT,
        fontSize: int = DEFAULT_FONT_SIZE,
        dimensions: tuple[float, float] = DEFAULT_DIMENSIONS,
        position: tuple[float, float] = DEFAULT_POSITION,
        color: kn.Color = DEFAULT_COLOR,
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

    def createMenuButton(
        self,
        content: str = DEFAULT_CONTENT,
        fontSize: int = DEFAULT_FONT_SIZE,
        dimensions: tuple[float, float] = DEFAULT_DIMENSIONS,
        position: tuple[float, float] = DEFAULT_POSITION,
        color: kn.Color = DEFAULT_COLOR,
        activeColor: kn.Color = DEFAULT_ACTIVE_COLOR,
    ) -> MenuButton:
        """
        Creates a MenuButton shape with optional content, font size, dimensions, position, color, and active color.
        Note: MenuButton uses kraken-clean font and size 24 by default. To change font size, use setFontSize() on the returned MenuButton.
        """
        button = MenuButton()
        button.setContent(content).setFontSize(fontSize).setDimensions(
            dimensions[0], dimensions[1]
        ).setPosition(position[0], position[1]).setColor(color)
        button.setActiveColor(activeColor).setColor(color)
        return button
