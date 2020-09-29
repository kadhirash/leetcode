class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_s = []

    def push(self, x: int) -> None:
        self.s.append(x)
        if not self.min_s or x < self.min_s[-1][0]:
            self.min_s.append([x,1])
        elif self.min_s[-1][0] == x:
            self.min_s[-1][1] += 1

    def pop(self) -> None:
        if self.min_s[-1][0] == self.s[-1]:
            self.min_s[-1][1] -= 1
        if self.min_s[-1][1] == 0:
            self.min_s.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()