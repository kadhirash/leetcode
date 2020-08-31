class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_s = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_s or x <=self.min_s[-1]:
            self.min_s.append(x)
    def pop(self) -> None:
        if self.min_s[-1] == self.stack[-1]:
            self.min_s.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()