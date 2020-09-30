class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        stack.append(('#',0))
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c,1])
                
        ans = ''
        for c in range(len(stack)):
            ans+= stack[c][0] * stack[c][1]
        return ''.join(ans)