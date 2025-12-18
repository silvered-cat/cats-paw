from .Rectangle import Rectangle
from .TextBox import TextBox
import pykraken as kn
from .MenuButton import MenuButton
from .UpdatingTextBox import UpdatingTextBox


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

    def createRectangle(self) -> Rectangle:
        """Creates a Rectangle shape with optional dimensions, position, and color."""
        rect = Rectangle()
        rect.setDimensions(DEFAULT_DIMENSIONS[0], DEFAULT_DIMENSIONS[1]).setPosition(
            DEFAULT_POSITION[0], DEFAULT_POSITION[1]
        ).setColor(DEFAULT_COLOR)
        return rect

    def createTextBox(self) -> TextBox:
        """
        Creates a TextBox shape with optional content, font size, dimensions, position, and color.
        Note: TextBox uses kraken-clean font and size 24 by default. To change font size, use setFontSize() on the returned TextBox.
        """
        rect = TextBox()
        rect.setContent(DEFAULT_CONTENT).setFontSize(DEFAULT_FONT_SIZE).setDimensions(
            DEFAULT_DIMENSIONS[0], DEFAULT_DIMENSIONS[1]
        ).setPosition(DEFAULT_POSITION[0], DEFAULT_POSITION[1]).setColor(DEFAULT_COLOR)
        return rect

    def createMenuButton(self) -> MenuButton:
        """
        Creates a MenuButton shape with optional content, font size, dimensions, position, color, and active color.
        Note: MenuButton uses kraken-clean font and size 24 by default. To change font size, use setFontSize() on the returned MenuButton.
        """
        button = MenuButton()
        button.setContent(DEFAULT_CONTENT).setFontSize(DEFAULT_FONT_SIZE).setDimensions(
            DEFAULT_DIMENSIONS[0], DEFAULT_DIMENSIONS[1]
        ).setPosition(DEFAULT_POSITION[0], DEFAULT_POSITION[1]).setColor(DEFAULT_COLOR)
        button.setActiveColor(DEFAULT_ACTIVE_COLOR).setColor(DEFAULT_COLOR)
        return button

    def createUpdatingTextBox(self) -> UpdatingTextBox:
        """
        This is a TextBox that updates its content every frame by calling a getter method that returns a string.
        The bound function must not have any parameters and must return a string.
        All the default parameters of TextBox apply here as well.
        """
        rect = UpdatingTextBox()
        rect.setContent(DEFAULT_CONTENT).setFontSize(DEFAULT_FONT_SIZE).setDimensions(
            DEFAULT_DIMENSIONS[0], DEFAULT_DIMENSIONS[1]
        ).setPosition(DEFAULT_POSITION[0], DEFAULT_POSITION[1]).setColor(DEFAULT_COLOR)
        return rect
