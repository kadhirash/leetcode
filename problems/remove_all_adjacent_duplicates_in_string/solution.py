class Solution:
    def removeDuplicates(self, S: str) -> str:
        # Clarifications:
            # S is all lowercase letters
            # each answer is unique
        # To Do:
            # return S w/o duplicates
        # Example:
            # abbaca
                # aaca
                # ca
        # Strategy:
            # Use a stack to store the answer 
            # Iterate through the string, and check top char of stack with the next char
                # if same then pop off (abb)
            # else, append to stack
            # return answer as string! 
                # ''.join -> python
        
    
        ans = []
        for char in S:
            if ans and ans[-1] == char:
                ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)