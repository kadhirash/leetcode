class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # use 2 stacks, 1 for ans and 1 to hold the "(.)"
        stack, ans = [], []
        for i in range(len(s)):
            if s[i] == '(': # if left
                stack.append(i) # append the index
                ans.append(s[i])
            elif s[i] == ')': # if right
                if stack: # if stack already exists 
                    stack.pop() # pop off right and append to ans
                    ans.append(s[i])
                else:   # else just append space since no matching left
                    ans.append('') 
            else: # if neither left or right, then append value to ans
                ans.append(s[i])
                
        for i in stack: # ))((  -> example 3 
            ans[i] = '' # just give spaces 
        
        return ''.join(ans)
        
        