import pykraken as kn


class Timer:
    """
    A class that depends on the pyKraken library.
    Provides a set of APIs useful for rendering text. Prone to weird behaviors due to using real time opposed to the Kraken Timer class.
    """

    def __init__(self) -> None:
        self._marker = 0.00
        self._timeLength = 0.00
        self._pausedTime = 0.00
        self._isPaused = True
        self._resetLength = 0.00

    def setTimer(self, time: float):
        """Sets the amount of time for the countdown."""
        self._timeLength = time
        self._resetLength = time

    def getTimeRemaining(self) -> float:
        """Returns the difference between calling start and the internally set time."""
        if self._isPaused:
            return self._pausedTime
        return self._marker - kn.time.get_elapsed()

    def start(self):
        """Begins the countdown by setting an internal reference to the start time."""
        self._isPaused = False
        self._marker = kn.time.get_elapsed() + self._timeLength

    def isFinished(self) -> bool:
        """Returns a boolean based on remaining time."""
        return self.getTimeRemaining() <= 0.00

    def pause(self):
        """Pauses the timer by saving the remaining time."""
        self._timeLength = self.getTimeRemaining()
        self._pausedTime = self.getTimeRemaining()
        self._isPaused = True

    def restart(self):
        """Resets the Timer by re inputting the value provided to setTimer."""
        self.setTimer(self._resetLength)
