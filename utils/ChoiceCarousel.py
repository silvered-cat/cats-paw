from .ChoiceEnum import ChoiceEnum


class ChoiceNode:
    def __init__(self, data: ChoiceEnum):
        self.choice: ChoiceEnum = data
        self.next: ChoiceNode | None = None
        self.previous: ChoiceNode | None = None


class ChoiceCarousel:
    """
    A wrapper for a circular double linked list of type ChoiceEnum. Has all ChoiceEnums except NONE.
    Note: does not have any None references in the list and will trigger infinite while loops.
    """

    def __init__(self):
        self._head: ChoiceNode | None = None
        self._current: ChoiceNode | None
        self._initList()

    def _initList(self):
        """Internal method to add all ChoiceEnums to the list."""
        self._addNewNode(ChoiceNode(ChoiceEnum.CLAW))
        self._addNewNode(ChoiceNode(ChoiceEnum.SMACK))

        lastNode = ChoiceNode(ChoiceEnum.SWIPE)
        self._addNewNode(lastNode)

        # This will make a circular linked list.
        lastNode.next = self._head
        self._current = self._head
        if self._head is None:
            raise ValueError(
                "_head attribute in ChoiceCarousel is None when expecting ChoiceNode."
            )
        self._head.previous = lastNode

    def _addNewNode(self, node: ChoiceNode):
        """Internal method to add a new node."""
        if self._head is None:
            self._head = node
            return

        currentNode: ChoiceNode | None = self._head

        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = node
        node.previous = currentNode

    def nextNode(self):
        """
        Updates the current attribute to the next ChoiceEnum.
        Will recycle to the head automatically.
        """
        if self._current is None:
            return
        self._current = self._current.next

    def previousNode(self):
        """
        Updates the current attribute to the previous ChoiceEnum.
        Will recycle to the head automatically.
        """
        if self._current is None:
            return
        self._current = self._current.previous

    def getCurrentChoice(self) -> ChoiceEnum:
        """Gets the current ChoiceEnum."""
        if self._current is None:
            return ChoiceEnum.NONE
        return self._current.choice
