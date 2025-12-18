from .ChoiceEnum import ChoiceEnum


class ChoiceNode:
    def __init__(self, data: ChoiceEnum):
        self.choice: ChoiceEnum = data
        self.next: ChoiceNode | None = None


class ChoiceCarousel:
    def __init__(self):
        self._head: ChoiceNode | None = None
        self._current: ChoiceNode | None = ChoiceNode(ChoiceEnum.NONE)
        self._initList()

    def _initList(self):
        self._addNewNode(ChoiceNode(ChoiceEnum.CLAW))
        self._addNewNode(ChoiceNode(ChoiceEnum.SMACK))

        lastNode = ChoiceNode(ChoiceEnum.SWIPE)
        self._addNewNode(lastNode)

        # This will make a circular linked list.
        lastNode.next = self._head

    def _addNewNode(self, node: ChoiceNode):

        if self._head is None:
            self._head = node

        currentNode: ChoiceNode | None = self._head

        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = node

    def nextNode(self):
        if self._current is None:
            return
        self._current = self._current.next

    def getCurrentChoice(self) -> ChoiceNode | None:
        return self._current
