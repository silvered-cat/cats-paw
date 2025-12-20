from .ChoiceMapping import choice_mapping
from .OutcomeEnum import OutcomeEnum
from .ChoiceEnum import ChoiceEnum


class OutcomeCalculator:
    """
    Static class with methods to determine the outcome of the choice enums.
    """

    @staticmethod
    def determineOutcome(
        playerChoice: ChoiceEnum, opponentChoice: ChoiceEnum
    ) -> OutcomeEnum:
        """
        Static method that outputs an OutcomeEnum relative to the player

        Example: Player chose SMACK, NPC chose SWIPE, result is WIN because the player won.
        """
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
        """
        Static method used to determine what ChoiceEnum should be used to defeat the target.
        Consumed by NPCs.
        """
        return choice_mapping[selection]
