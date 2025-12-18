import enum


class StatusEnums(enum.IntEnum):
    PAUSED = enum.auto()
    IN_PROGRESS = enum.auto()
    START = enum.auto()
    END = enum.auto()
