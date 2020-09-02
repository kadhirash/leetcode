class Solution:
    def decodeString(self, s: str) -> str:
        stack, num = [], []
        stack.append([ [],1 ])
        #print(stack)
        for chars in s:
            if chars.isdigit():
                num.append(chars)
            elif chars == '[':
                stack.append([ [], int("".join(num)) ])
                #print(stack)
                num = []
            elif chars == ']':
                st, k = stack.pop()
                stack[-1][0].extend((st*k))
                #print(stack)
            else:
                stack[-1][0].append(chars)
                #print(stack)
        return "".join(stack[0][0])
                