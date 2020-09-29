class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack.append('#')
        
        mapping = {')':'(', ']':'[', '}':'{'}
        
        for val in s:
            if val in mapping:
                if stack.pop() != mapping[val]:
                    return False
            else:
                stack.append(val)
            
        return len(stack) == 1