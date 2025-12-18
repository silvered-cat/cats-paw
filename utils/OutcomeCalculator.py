from .ChoiceMapping import choice_mapping
from .OutcomeEnum import OutcomeEnum
from .ChoiceEnum import ChoiceEnum


class OutcomeCalculator:

    @staticmethod
    def determineOutcome(
        playerChoice: ChoiceEnum, opponentChoice: ChoiceEnum
    ) -> OutcomeEnum:
        if playerChoice == ChoiceEnum.NONE or opponentChoice == ChoiceEnum.NONE:
            raise ValueError(
                "Player should have made a choice. Instead got default enum NONE."
            )

        if playerChoice == opponentChoice:
            return OutcomeEnum.DRAW

        winningChoice = choice_mapping[playerChoice]

        if winningChoice == opponentChoice:
            return OutcomeEnum.WIN
        else:
            return OutcomeEnum.LOSE

    @staticmethod
    def getWinningOutcome(selection: ChoiceEnum) -> ChoiceEnum:
        return choice_mapping[selection]
