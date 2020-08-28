class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min_items = []
        
    def push(self, x: int) -> None:
        self.items.append(x)
        if not self.min_items or x <= self.min_items[-1]:
            self.min_items.append(x)
        
    def pop(self) -> None:
        if self.min_items[-1] == self.items[-1]:
            self.min_items.pop()
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_items[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()