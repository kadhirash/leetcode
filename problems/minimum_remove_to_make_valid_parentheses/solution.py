class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # keep track of left or right
        # if left then appen 
        
        
        stack = []
        ans = []
        for c in s:
            ans.append(c)
            
            
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    ans[i] = '#' # dummy variable
            
        while stack: # where its all ((
            ans[stack.pop()] = '#'
            
            
        
        return ''.join(ans).replace('#', '')
                