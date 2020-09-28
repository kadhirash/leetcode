class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
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
                    ans[i] = '#'
                    
        while stack:
            ans[stack.pop()] = '#'
            
            
        
        return ''.join(ans).replace('#', '')