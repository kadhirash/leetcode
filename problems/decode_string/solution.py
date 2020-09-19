class Solution:
    def decodeString(self, s: str) -> str:
        
        # create two stack, one for the numbers and one for everything else
        
        stack, num = [], []
        # append empty stack and number 1 to the stack
        stack.append([ [], 1])
        for chars in s:
            # numbers -> both stacks
            if chars.isdigit():
                num.append(chars)
            # if left bracket
            elif chars == '[':
                stack.append( [ [], int("".join(num)) ]  ) # append the empty stack as well as the previous value from numbers
                num = [] # reset num stack
            
            # right bracket
            elif chars == ']':
                st, k = stack.pop() # pop off string + k (num) from stack since 2 pos. in stack
                
                stack[-1][0].extend((st*k)) # extend to the first pos. of tuple in stack the vals. of the popped off st*k 
            
            else:
                stack[-1][0].append(chars) # if not a [] or number append only to first position of tuple in stack
        return ''.join(stack[0][0]) # return the string 