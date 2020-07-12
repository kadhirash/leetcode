class Solution:
    def isValid(self, s: str) -> bool:
        # open brackets <--> closed brackets of same type, and closed in correct order
        # { [ ]}
        
        
        # create a stack -> LIFO of the input
        # input: (), {}, [ ]
        # check if it leaves in correct order --> true, else false
        # empty string -> true
        
        if len(s) < 1:
            return True
        stack = [ ]
        
        hash_map = {")":"(", "}": "{", "]": "[" }
        
        for i in s:
            if i in hash_map:
                top = stack.pop() if stack else '#'
            
                if hash_map[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack
                