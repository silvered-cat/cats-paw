from .ChoiceEnum import ChoiceEnum


"""
A dictionary that maps a ChoiceEnum to the ChoiceEnum that it 'defeats'.

Strengths:
- SMACK defeats SWIPE analogous to rock beats scissors
- SWIPE defeats SMACK analogous to scissors beats paper
- CLAW defeats SWIPE analogous to paper beats rock
"""


choice_mapping = {
    ChoiceEnum.SMACK: ChoiceEnum.SWIPE,
    ChoiceEnum.SWIPE: ChoiceEnum.CLAW,
    ChoiceEnum.CLAW: ChoiceEnum.SMACK,
}
