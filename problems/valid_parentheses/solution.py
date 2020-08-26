class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol in "([{":
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if not self.matches(stack.pop(),symbol):
                        return False
        return len(stack) == 0
    
    def matches(self,symbol_left,symbol_right):
        all_left = "({["
        all_right = ")}]"
        return all_left.index(symbol_left) == all_right.index(symbol_right)