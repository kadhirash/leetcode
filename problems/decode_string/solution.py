class Solution:
    def decodeString(self, s: str) -> str:
        stack, curr_str, curr_count = [], '', 0
        
        for c in s:
            
            if c == '[':
                stack.append(curr_str)
                stack.append(curr_count)
                curr_str = ''
                curr_count = 0
            elif c == ']':
                prev_count = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + prev_count * curr_str
            elif c.isdigit():
                curr_count = 10 * curr_count + int(c)
            else: # character
                curr_str += c
                
        return curr_str
                