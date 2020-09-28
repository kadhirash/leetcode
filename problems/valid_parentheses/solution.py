class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []        
        
        mapping = {')': '(' , ']': "[" , "}": "{"}
            

        for brack in s:
            if brack in mapping:
                if stack:
                    top_elem = stack.pop()
                else:
                    top_elem = '#'
                    
                if mapping[brack] != top_elem:
                    return False
            else:
                stack.append(brack)
            
        return not stack
                