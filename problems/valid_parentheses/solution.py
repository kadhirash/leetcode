class Solution:
    def isValid(self, s: str) -> bool:
        # strategy:
            # create a mapping of brackets
                # [], (), {}
            # use a stack to keep track of brackets
            
        
        
        stack = []
        
        mapping = {")": "(", "}" : "{", "]" : "["}
        
        for bracket in s:
            if bracket in mapping:
                if stack:
                    top_elem = stack.pop()
                else:
                    top_elem = '#'
            
                if mapping[bracket] != top_elem:
                    return False
            else:
                stack.append(bracket)
                
        return not stack
                