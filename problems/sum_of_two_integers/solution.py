class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 0001
        # 0010
        # 0011
        
        
        # 1 0010 --> # 0 1001
        #   0011     #   001
        #   0001
        
        mask = 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)