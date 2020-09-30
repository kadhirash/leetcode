class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # q/a:
            # return "" if not s
        # strat:
            # stack
                # "(" ")"
            # ans 
                # s
            # '%' -> dummy variable
            # replace dummy variable with a space
            
            # 
            # ans = [%%%%]
            
        stack = []
        ans = []
        for c in s:
            ans.append(c)
        
        for c in range(len(s)):
            if s[c] == '(':
                stack.append(c)
            elif s[c] == ')':
                if stack:
                    stack.pop()
                else:
                    ans[c] = '%'
        
        while stack:
            ans[stack.pop()] = '%'
            
        return ''.join(ans).replace('%','')