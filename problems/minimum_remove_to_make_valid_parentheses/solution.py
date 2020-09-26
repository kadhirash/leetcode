class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, ans = [],[]
        for c in s:
            ans.append(c)
            
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) # index
            elif s[i] == ')':
                if stack:
                    stack.pop() # remove
                else:
                    ans[i] = '#' # add dummy var
        
        while stack: # all '('
            ans[stack.pop()] = '#' # set the values to dummy var
            
        
        return ''.join(ans).replace('#',"")
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = []
#         res = []
#         for c in s:
#             res.append(c)
        
#         for i in range(len(s)):
#             if s[i] == '(':
#                 stack.append(i)
#             elif s[i] == ')':
#                 if stack:
#                     stack.pop()
#                 else:
#                     res[i] = '#'
#         while stack: # all open
#             res[stack.pop()] = '#'
            
#         return "".join(res).replace('#',"")