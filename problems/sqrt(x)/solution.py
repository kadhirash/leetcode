class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right-left) // 2
            
            ans = mid * mid
            
            if ans == x:
                return mid
            elif ans < x:
                left = mid + 1
            elif ans > x:
                right = mid - 1
        
        return right