class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = []
        for chars in S:
            if ans and ans[-1] == chars: # if ans and chars is in the top of the ans stack
                ans.pop() # pop off char
            else:
                ans.append(chars) # append char
        return ''.join(ans)
    
    