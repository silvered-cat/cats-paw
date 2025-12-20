import enum


class StatusEnums(enum.IntEnum):
    """
    Enums that indicate the status of the battle round.

    Enums:
        START - A new round is queued up to begin.
        IN_PROGRESS - The round is currently executing
        PAUSED - The round has been paused via escape menu or something similar.
        END - The round is over and results need to be calculated.
    """

    PAUSED = enum.auto()
    IN_PROGRESS = enum.auto()
    START = enum.auto()
    END = enum.auto()
