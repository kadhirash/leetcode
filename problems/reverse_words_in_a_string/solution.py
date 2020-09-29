class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = s.split()
        stack = []
        
        for i in range(len(new_str)-1,-1,-1):
            if new_str[i]:
                stack.append(new_str[i])
                
        return ' '.join(stack)