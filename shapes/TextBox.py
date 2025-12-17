import pykraken as kn
from .Rectangle import Rectangle


class TextBox(Rectangle):
    """
    A TextBox rectangle shape that can display text.
    Inherits from Rectangle and Shape.
    Attributes:
        _font (Font): The font used for the text. Needs to maintain a reference to avoid garbage collection by pykraken.
        _content (str): The text content to display.
        _anchor (Anchor): The anchor point for text alignment. Defaults to the center of the Rectangle.
    """

    def __init__(self):
        super().__init__()
        self._font = kn.Font("kraken-clean", 24)
        self._content = "I love Cats!!"
        self._anchor = kn.Anchor.CENTER
        text = kn.Text(self._font)
        self._text = text

    def draw(self) -> None:
        """Draw the TextBox shape along with its text content."""
        super().draw()
        self._text.draw(self.getPosition(), self.getAnchor())

    def setAnchor(self, anchor: kn.Anchor) -> TextBox:
        """Changes the anchor point for text alignment."""
        self._anchor = anchor
        return self

    def _updateText(self) -> None:
        """Internal method to sync text between TextBox and Text class."""
        self._text.text = self.getContent()

    def getAnchor(self) -> kn.Anchor:
        """Get the current anchor point for text alignment. Relative to the Rectangle."""
        return self._anchor

    def setContent(self, content: str) -> TextBox:
        """Set the text content of the TextBox."""
        self._content = content
        self._updateText()
        return self

    def getContent(self) -> str:
        """Get the text content of the TextBox."""
        return self._content

    def setFont(self, font: str) -> TextBox:
        """Set the font of the TextBox text."""
        self._font = kn.Font(font, self._font.pt_size)
        return self

    def getFont(self) -> kn.Font:
        """Get the saved Font instance."""
        return self._font

    def setFontSize(self, size: int) -> TextBox:
        """Changes the font size of the TextBox text."""
        self._font.pt_size = size
        return self

    def getFontSize(self) -> int:
        """Get the font size of the TextBox text."""
        return self._font.pt_size

    def setTextColor(self, color: kn.Color) -> TextBox:
        """Set the color of the TextBox text."""
        self._text.color = color
        return self
