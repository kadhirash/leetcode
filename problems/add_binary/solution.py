class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 0 + 0 --> 0
        # 0 + 1 --> 1
        # 1 + 0 --> 0
        # 1 + 1 --> 0, carry 1
        
        
        # Loop through a
        # Loop through b
        # 4 if statements
        
        x,y = int(a,2), int(b,2) # answer, carry, respectively
        
        while y != 0:
            answer = x^y # XOR
            carry = (x & y) << 1 # AND + bit-shift left
            x , y = answer , carry 
        return bin(x)[2:]