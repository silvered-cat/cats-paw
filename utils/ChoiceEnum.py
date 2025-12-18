import enum


class ChoiceEnum(enum.Enum):
    """
    These are the possible choices in the game.
    """

    SMACK = enum.auto()  # rock
    CLAW = enum.auto()  # paper
    SWIPE = enum.auto()  # scissors
    NONE = enum.auto()  # no choice made
