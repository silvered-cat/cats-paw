class CharNode:
    def __init__(self, c: str):
        self.char = c
        self.next: CharNode | None = None


class MessageMarquee:
    def __init__(self, message: str):
        self._head: None | CharNode = None
        self._current: None | CharNode = None
        lastNode: None | CharNode = None

        # Make single linked list
        for c in message:
            lastNode = self._appendCharNode(c)

        # Forced check for type checker
        if lastNode is not None:
            # This makes the list a circular Linked List
            lastNode.next = self._head
        # Setting index 0 to the start of the List.
        self._current = self._head

    def getChar(self) -> str:
        # Gets and outputs the next char in the marquee before advancing to the next list.
        if self._current is None:
            raise TypeError("Expected an instance of CharNode but found None.")
        c = self._current.char
        self._current = self._current.next
        return c

    def _appendCharNode(self, c: str) -> CharNode:
        if self._head is None:
            self._head = CharNode(c)
            return self._head

        current = self._head

        while current.next is not None:
            current = current.next

        current.next = CharNode(c)
        return current.next
