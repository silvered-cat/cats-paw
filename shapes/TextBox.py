import pykraken as kn
from .Rectangle import Rectangle


class TextBox(Rectangle):
    """
    A TextBox rectangle shape that can display text.
    Inherits from Rectangle and Shape.
    Attributes:
        _font (Font): The font used for the text.
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
        super().draw()

        self._text.draw(self.getPosition(), self.getAnchor())

    def setAnchor(self, anchor: kn.Anchor) -> TextBox:
        self._anchor = anchor
        return self

    def _updateText(self) -> None:
        self._text.text = self.getContent()

    def getAnchor(self) -> kn.Anchor:
        return self._anchor

    def setContent(self, content: str) -> TextBox:
        self._content = content
        self._updateText()
        return self

    def getContent(self) -> str:
        return self._content

    def setFont(self, font: str) -> TextBox:

        self._font = kn.Font(font, self._font.pt_size)
        return self

    def getFont(self) -> kn.Font:
        return self._font

    def setFontSize(self, size: int) -> TextBox:
        self._font.pt_size = size
        return self

    def getFontSize(self) -> int:
        return self._font.pt_size
