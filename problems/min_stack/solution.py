class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []

    def push(self, x: int) -> None:
        if not self._items:
            self._items.append((x,x))
            return
        curr_min = self._items[-1][-1]
        self._items.append((x, min(x, curr_min)))

    def pop(self) -> None:
        self._items.pop()

    def top(self) -> int:
        return self._items[-1][0]

    def getMin(self) -> int:
        return self._items[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()