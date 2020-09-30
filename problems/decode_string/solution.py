class Solution:
    def decodeString(self, s: str) -> str:
        # q/a:
            # k == number
            # 1 -9 or > ?
                # can be greater
        # strat:
            # stack, curr_str, curr_count
            # 1) '['
                # curr_str, curr_count 
                # reset
            # 2) ']'
                # pop count , pop str
            # 3) digit
                # 10 + int(c)
                    # 2[a1[b]] --> 21[ab]
            # 4 ) character
                # add to string
                
                
        stack = []
        curr_str = ''
        curr_count = 0
        
        for c in s:
            if c == '[':
                stack.append(curr_str)
                stack.append(curr_count)
                curr_str = ''
                curr_count = 0
            elif c == ']':
                prev_count = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_str * prev_count
            elif c.isdigit():
                curr_count = 10 * curr_count + int(c)
            else: # char
                curr_str += c
        
        return curr_str
            
            
            