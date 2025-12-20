import enum


class ScreensEnum(enum.IntEnum):
    """
    Enum for different screens in the game. Typically used to retrieve
    the correct screen instance from a dictionary mapping.
    """

    MENU = enum.auto()
    BATTLE = enum.auto()
    RESOLVE = enum.auto()
    GAMEOVER = enum.auto()
    VICTORY = enum.auto()
