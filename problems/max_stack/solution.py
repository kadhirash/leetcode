class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        if self.stack and x >= self.stack[self.stack[-1][1]][0]:
            i = len(self.stack) # index of max
        else:
            i = self.stack[-1][1] if self.stack else 0
        self.stack.append((x, i))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[self.stack[-1][1]][0]

    def popMax(self) -> int:
        index = self.stack[-1][1]  # index where the max exists
        result = self.stack[index][0]  # max value to return
        new_max = self.stack[self.stack[index-1][1]][0] if index > 0 else -float('inf')
        # Scan the stack starting at 'index' to recompute the max values and shift all
        # values to the left by one:
        for i in range(index, len(self.stack)-1):
            if self.stack[i+1][0] >= new_max:
                new_max = self.stack[i+1][0]
                self.stack[i] = (self.stack[i+1][0], i)
            else:
                self.stack[i] = (self.stack[i+1][0], self.stack[i-1][1])
        self.stack.pop()
        return result


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()