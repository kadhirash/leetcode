class Solution:
    def reverse(self, x: int) -> int:
        
        ans = 0

        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        while x:
            ans = ans * 10 + x % 10
            x //= 10

        
        if ans > pow(2,31):
            return 0
        else:
            return ans * sign
