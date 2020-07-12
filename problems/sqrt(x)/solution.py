class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left,right = 2, x // 2
        
        while left <= right:
            middle = left + (right-left) // 2
            
            num = middle * middle
            
            if num > x:
                right = middle - 1
            elif num < x:
                left = middle + 1
            elif num == x:
                return middle
        return right