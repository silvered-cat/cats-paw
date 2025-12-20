from state.State import State
from screens.screensEnum import ScreensEnum
import pykraken as kn
from utils.ChoiceEnum import ChoiceEnum
from utils.StatusEnums import StatusEnums

INIT_ROUND_TIME_LIMIT_SECONDS = 10.0  # This it to prevent errors during init
# POINTS_TO_VICTORY = 3
POINTS_TO_VICTORY = 3


class Game(State):
    def __init__(self):
        self._playerScore = 0
        self._npcScore = 0
        self._current_screen: ScreensEnum
        self._timeMarker = 0.00  # Time when the round started
        self._roundTimeLimitSeconds = INIT_ROUND_TIME_LIMIT_SECONDS
        self._playerChoice = ChoiceEnum.NONE
        self._opponentChoice = ChoiceEnum.NONE
        self._roundStatus: StatusEnums = StatusEnums.START
        initialScreen = ScreensEnum.MENU
        self.setCurrentScreen(initialScreen)
        self._pointsToWin = POINTS_TO_VICTORY

    def getPointsToWin(self) -> int:
        return self._pointsToWin

    def setPointsToWin(self, points: int):
        self._pointsToWin = points

    def getRoundStatus(self) -> StatusEnums:
        return self._roundStatus

    def setRoundStatus(self, status: StatusEnums):
        self._roundStatus = status

    def setPlayerChoice(self, choice: ChoiceEnum) -> None:
        self._playerChoice = choice

    def getPlayerChoice(self) -> ChoiceEnum:
        return self._playerChoice

    def setOpponentChoice(self, choice: ChoiceEnum) -> None:
        self._opponentChoice = choice

    def getOpponentChoice(self) -> ChoiceEnum:
        return self._opponentChoice

    def getWindowSize(self) -> tuple[float, float]:
        win = kn.window.get_size()
        return (win.x, win.y)

    def setCurrentScreen(self, screen: ScreensEnum) -> Game:
        self._current_screen = screen
        return self

    def getCurrentScreen(self) -> ScreensEnum:
        return self._current_screen

    def getNPCScore(self) -> int:
        return self._npcScore

    def getPlayerScore(self) -> int:
        return self._playerScore

    def incrementNPCScore(self) -> None:
        self._npcScore += 1

    def incrementPlayerScore(self) -> None:
        self._playerScore += 1

    def resetScores(self) -> None:
        self._npcScore = 0
        self._playerScore = 0

    def setRoundTimeLimit(self, timeLimitSeconds: float) -> None:
        self._roundTimeLimitSeconds = timeLimitSeconds

    def startCountdownTimer(self) -> None:
        self._timeMarker = kn.time.get_elapsed() + self._roundTimeLimitSeconds

    def getRemainingTime(self) -> float:
        elapsedTime = self._timeMarker - kn.time.get_elapsed()
        return elapsedTime

    def isTimeUp(self) -> bool:
        elapsedTime = self.getRemainingTime()
        return elapsedTime <= 0.00
