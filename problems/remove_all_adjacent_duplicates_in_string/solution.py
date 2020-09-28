class Solution:
    def removeDuplicates(self, S: str) -> str:
        # abbaca 
            # [ca]
            
            
        
        
        stack = []
        
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)