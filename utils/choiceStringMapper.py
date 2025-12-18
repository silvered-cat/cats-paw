from utils.ChoiceEnum import ChoiceEnum

choiceDict: dict[ChoiceEnum, str] = {
    ChoiceEnum.SMACK: "SMACK!",
    ChoiceEnum.CLAW: "CLAW!",
    ChoiceEnum.SWIPE: "SWIPE!",
}


def getChoiceString(choice: ChoiceEnum) -> str:
    return choiceDict[choice]
